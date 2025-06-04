from flask import Flask, render_template, request, send_file, session
from pymongo import MongoClient
from fpdf import FPDF
import io
from collections import defaultdict

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'

@app.template_filter('char_from_index')
def char_from_index(index):
    return chr(65 + index) if isinstance(index, int) and 0 <= index < 26 else str(index)

client = MongoClient("mongodb://localhost:27017/")
db = client['question_paper']
collection = db['questions']

@app.route('/')
def home():
    return render_template('form.html')

def create_dynamic_groups(questions, selected_units):
    # Group questions by unit first, then by unit_group
    unit_groups = defaultdict(lambda: defaultdict(list))
    
    for q in questions:
        unit = q['unit']
        unit_group = q.get('unit_group', '1')
        unit_groups[unit][str(unit_group)].append(q)

    # Create final grouped structure maintaining unit order
    grouped = {}
    current_group_id = 1
    
    # Sort units to maintain order (Unit 1, Unit 2, etc.)
    sorted_units = sorted(selected_units, key=lambda x: int(x.split()[-1]) if x.split()[-1].isdigit() else float('inf'))
    
    for unit in sorted_units:
        if unit not in unit_groups:
            continue
            
        # Sort unit groups within each unit
        sorted_unit_groups = sorted(unit_groups[unit].keys(), key=lambda x: int(x) if x.isdigit() else float('inf'))
        
        for unit_group in sorted_unit_groups:
            group_questions = unit_groups[unit][unit_group]
            if group_questions:
                # Sort questions within group by option_id
                sorted_questions = sorted(group_questions, key=lambda x: x.get('option_id', 0))
                
                # Add metadata to questions
                for q in sorted_questions:
                    q['original_unit_group'] = q.get('unit_group', '1')
                    q['original_unit'] = unit
                    q['_id'] = str(q['_id'])
                
                grouped[current_group_id] = sorted_questions
                current_group_id += 1
    
    return grouped

def get_questions_for_units(subject, units, difficulty="easy", q_type="theory", examtype="endsem"):
    try:
        base_query = {
            "subject": subject,
            "difficulty": difficulty,
            "type": q_type,
            "examtype": examtype,
            "unit": {"$in": units}
        }
        
        print(f"Query: {base_query}")  # Debug print
        questions = list(collection.find(base_query))
        print(f"Found {len(questions)} questions")  # Debug print
        
        return questions
    except Exception as e:
        print(f"ERROR: Database query error: {e}")
        return []

@app.route('/generate', methods=['POST'])
def generate():
    try:
        subject = request.form['subject'].strip().lower()
        units = request.form.getlist('units')
        difficulty = request.form['difficulty'].strip().lower()
        q_type = request.form['type'].strip().lower()
        examtype = request.form['examtype'].strip().lower()

        if not units:
            units = ["Unit 1", "Unit 2"] if examtype == 'insem' else ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]

        print(f"Searching for: subject={subject}, units={units}, difficulty={difficulty}, type={q_type}, examtype={examtype}")

        questions = get_questions_for_units(subject, units, difficulty, q_type, examtype)
        if not questions:
            return render_template('result.html', grouped={}, examtype=examtype, error="No questions found for the given criteria.")

        grouped = create_dynamic_groups(questions, units)
        if not grouped:
            return render_template('result.html', grouped={}, examtype=examtype, error="Could not group questions properly.")

        # Filter final questions for preview just like PDF logic
        filtered_grouped = {}

        if examtype == 'endsem':
            for group_id, questions in grouped.items():
                unit = questions[0].get('original_unit', questions[0].get('unit', 'Unknown'))

                if unit == "Unit 1" or unit == "Unit 2":
                    # 2 compulsory questions
                    filtered_grouped[group_id] = questions[:2]
                else:
                    # 2 questions of 4 marks, 4 of 6 marks
                    four_mark_qs = [q for q in questions if q.get('marks') == 4][:2]
                    six_mark_qs = [q for q in questions if q.get('marks') == 6][:4]
                    filtered_grouped[group_id] = four_mark_qs + six_mark_qs

        elif examtype == 'insem':
            for group_id, questions in grouped.items():
                filtered_grouped[group_id] = questions[:6]  # max 6 used in PDF logic

        # Save to session for /download
        session['grouped_questions'] = filtered_grouped
        session['selected_units'] = units
        session['form_data'] = {
            'subject': subject,
            'difficulty': difficulty,
            'type': q_type,
            'examtype': examtype
        }

        return render_template('result.html', grouped=filtered_grouped, examtype=examtype)

    except Exception as e:
        print(f"Generation error: {e}")
        return render_template('result.html', grouped={}, examtype='endsem', error=f"Server error: {str(e)}")


def clean_text(text):
    if not isinstance(text, str):
        text = str(text)
    
    # Simple character replacements using only ASCII characters
    text = text.replace(chr(8217), "'")  # right single quotation mark
    text = text.replace(chr(8220), '"')  # left double quotation mark  
    text = text.replace(chr(8221), '"')  # right double quotation mark
    text = text.replace(chr(8211), '-')  # en dash
    text = text.replace(chr(8212), '-')  # em dash
    text = text.replace(chr(8230), '...')  # horizontal ellipsis
    text = text.replace('Ω', 'Ohm')
    text = text.replace('α', 'alpha')
    text = text.replace('β', 'beta')
    text = text.replace('γ', 'gamma')
    text = text.replace('δ', 'delta')
    text = text.replace('ε', 'epsilon')
    text = text.replace('θ', 'theta')
    text = text.replace('λ', 'lambda')
    text = text.replace('μ', 'mu')
    text = text.replace('π', 'pi')
    text = text.replace('ρ', 'rho')
    text = text.replace('σ', 'sigma')
    text = text.replace('τ', 'tau')
    text = text.replace('φ', 'phi')
    text = text.replace('ω', 'omega')
    text = text.replace('°', ' deg')
    text = text.replace('µ', 'u')
    text = text.replace('≥', '>=')
    text = text.replace('≤', '<=')
    text = text.replace('≠', '!=')
    text = text.replace('×', 'x')
    text = text.replace('÷', '/')
    text = text.replace('∞', 'infinity')
    text = text.replace('∑', 'sum')
    text = text.replace('√', 'sqrt')
    text = text.replace('²', '^2')
    text = text.replace('³', '^3')
    
    try:
        text.encode('latin-1')
    except UnicodeEncodeError:
        text = text.encode('latin-1', errors='replace').decode('latin-1')
    return text

def _print_question_with_marks(pdf, question_line, marks, line_height):
    approx_marks_width = pdf.get_string_width(f"[{marks} marks]") + 5
    available_width_for_question = pdf.w - pdf.l_margin - pdf.r_margin - approx_marks_width
    pdf.set_x(pdf.l_margin)
    if pdf.get_string_width(question_line) > available_width_for_question:
        pdf.multi_cell(available_width_for_question, line_height, question_line, 0, 'L', False)
        pdf.set_xy(pdf.w - pdf.r_margin - approx_marks_width, pdf.get_y() - line_height)
        pdf.cell(approx_marks_width, line_height, f"[{marks} marks]", 0, 1, 'R')
    else:
        pdf.cell(available_width_for_question, line_height, question_line, 0, 0, 'L')
        pdf.cell(approx_marks_width, line_height, f"[{marks} marks]", 0, 1, 'R')

@app.route('/download', methods=['POST'])
def download():
    try:
        grouped = session.get('grouped_questions', {})
        selected_units = session.get('selected_units', [])
        form_data = session.get('form_data', {})

        if not grouped:
            return "No questions to generate PDF", 400

        examtype = form_data.get('examtype', 'insem').lower()
        subject = form_data.get('subject', 'Unknown').upper()
        total_marks = "60 Marks" if examtype == 'endsem' else "30 Marks"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, f'{subject} - {examtype.upper()} Question Paper ({total_marks})', 0, 1, 'C')
        pdf.ln(10)
        pdf.set_font('Arial', '', 12)
        line_height = 8

        # Get questions organized by unit
        unit_questions = defaultdict(list)
        for group_id, questions in grouped.items():
            if questions:
                unit = questions[0].get('original_unit', questions[0].get('unit', 'Unknown'))
                unit_questions[unit].extend(questions)

        def render_60_marks_pattern_fixed(pdf, unit_questions):
            """
            Fixed 60 marks pattern based on your database structure:
            Q1 (Unit 1 - Compulsory): A] 3 marks, B] 3 marks  
            Q2 (Unit 2 - Compulsory): A] 3 marks, B] 3 marks
            Q3 (Unit 3): A] 4 OR B] 4, C] 6 OR D] 6, E] 6 OR F] 6
            Q4 (Unit 4): A] 4 OR B] 4, C] 6 OR D] 6, E] 6 OR F] 6  
            Q5 (Unit 5): A] 4 OR B] 4, C] 6 OR D] 6, E] 6 OR F] 6
            """
            
            # Units 1 and 2 - Compulsory (6 marks each = 12 total)
            compulsory_units = ["Unit 1", "Unit 2"]
            for i, unit in enumerate(compulsory_units, 1):
                if unit in unit_questions:
                    questions = unit_questions[unit]
                    
                    # Header
                    pdf.set_font('Arial', 'B', 14)
                    pdf.cell(0, line_height, f"Q{i}. (Compulsory) - {unit}", ln=True)
                    pdf.ln(2)
                    pdf.set_font('Arial', '', 12)
                    
                    # A] 3 marks, B] 3 marks
                    if len(questions) >= 1:
                        _print_question_with_marks(pdf, f"A] {clean_text(questions[0]['question'])}", 3, line_height)
                        pdf.ln(1)
                    if len(questions) >= 2:
                        _print_question_with_marks(pdf, f"B] {clean_text(questions[1]['question'])}", 3, line_height)
                        pdf.ln(1)
                    
                    pdf.ln(6)
            
            # Units 3, 4, 5 - Choice questions (16 marks each = 48 total)
            choice_units = ["Unit 3", "Unit 4", "Unit 5"]
            for i, unit in enumerate(choice_units, 3):
                if unit in unit_questions:
                    questions = unit_questions[unit]
                    
                    # Group questions by marks and unit_group
                    questions_4_marks = [q for q in questions if q.get('marks') == 4]
                    questions_6_marks = [q for q in questions if q.get('marks') == 6]
                    
                    # Header
                    pdf.set_font('Arial', 'B', 14)
                    pdf.cell(0, line_height, f"Q{i}. - {unit}", ln=True)
                    pdf.ln(2)
                    pdf.set_font('Arial', '', 12)
                    
                    # A] 4 marks OR B] 4 marks
                    if len(questions_4_marks) >= 1:
                        _print_question_with_marks(pdf, f"A] {clean_text(questions_4_marks[0]['question'])}", 4, line_height)
                        pdf.ln(2)
                        
                        # OR separator
                        pdf.set_font('Arial', 'B', 12)
                        pdf.cell(0, line_height, "OR", 0, 1, 'C')
                        pdf.set_font('Arial', '', 12)
                        pdf.ln(1)
                        
                        if len(questions_4_marks) >= 2:
                            _print_question_with_marks(pdf, f"B] {clean_text(questions_4_marks[1]['question'])}", 4, line_height)
                        pdf.ln(3)
                    
                    # C] 6 marks OR D] 6 marks  
                    if len(questions_6_marks) >= 1:
                        _print_question_with_marks(pdf, f"C] {clean_text(questions_6_marks[0]['question'])}", 6, line_height)
                        pdf.ln(2)
                        
                        # OR separator
                        pdf.set_font('Arial', 'B', 12)
                        pdf.cell(0, line_height, "OR", 0, 1, 'C')
                        pdf.set_font('Arial', '', 12)
                        pdf.ln(1)
                        
                        if len(questions_6_marks) >= 2:
                            _print_question_with_marks(pdf, f"D] {clean_text(questions_6_marks[1]['question'])}", 6, line_height)
                        pdf.ln(3)
                    
                    # E] 6 marks OR F] 6 marks
                    if len(questions_6_marks) >= 3:
                        _print_question_with_marks(pdf, f"E] {clean_text(questions_6_marks[2]['question'])}", 6, line_height)
                        pdf.ln(2)
                        
                        # OR separator
                        pdf.set_font('Arial', 'B', 12)
                        pdf.cell(0, line_height, "OR", 0, 1, 'C')
                        pdf.set_font('Arial', '', 12)
                        pdf.ln(1)
                        
                        if len(questions_6_marks) >= 4:
                            _print_question_with_marks(pdf, f"F] {clean_text(questions_6_marks[3]['question'])}", 6, line_height)
                        pdf.ln(1)
                    
                    pdf.ln(6)

        def render_30_marks_pattern(pdf, unit_questions):
            """
            30 marks pattern:
            Q1 (Unit 1 - Compulsory): A] 3 marks, B] 4 marks
            Q2 (Unit 1 - Solve Any Two): A] 4 marks, B] 4 marks OR C] 4 marks, D] 4 marks  
            Q3 (Unit 2 - Compulsory): A] 3 marks, B] 4 marks
            Q4 (Unit 2 - Solve Any Two): A] 4 marks, B] 4 marks OR C] 4 marks, D] 4 marks
            """
            units_30 = ["Unit 1", "Unit 2"]
            question_num = 1
            
            for unit in units_30:
                if unit in unit_questions:
                    questions = unit_questions[unit]
                    
                    # Compulsory section
                    pdf.set_font('Arial', 'B', 14)
                    pdf.cell(0, line_height, f"Q{question_num}. (Compulsory) - {unit}", ln=True)
                    pdf.ln(2)
                    pdf.set_font('Arial', '', 12)
                    
                    if len(questions) >= 1:
                        _print_question_with_marks(pdf, f"A] {clean_text(questions[0]['question'])}", 3, line_height)
                        pdf.ln(1)
                    if len(questions) >= 2:
                        _print_question_with_marks(pdf, f"B] {clean_text(questions[1]['question'])}", 4, line_height)
                        pdf.ln(1)
                    
                    pdf.ln(6)
                    question_num += 1
                    
                    # Choice section
                    pdf.set_font('Arial', 'B', 14)
                    pdf.cell(0, line_height, f"Q{question_num}. (Solve Any Two) - {unit}", ln=True)
                    pdf.ln(2)
                    pdf.set_font('Arial', '', 12)
                    
                    if len(questions) >= 4:
                        _print_question_with_marks(pdf, f"A] {clean_text(questions[2]['question'])}", 4, line_height)
                        pdf.ln(1)
                        _print_question_with_marks(pdf, f"B] {clean_text(questions[3]['question'])}", 4, line_height)
                        pdf.ln(2)
                        
                        # OR
                        pdf.set_font('Arial', 'B', 12)
                        pdf.cell(0, line_height, "OR", 0, 1, 'C')
                        pdf.set_font('Arial', '', 12)
                        pdf.ln(1)
                        
                        if len(questions) >= 6:
                            _print_question_with_marks(pdf, f"C] {clean_text(questions[4]['question'])}", 4, line_height)
                            pdf.ln(1)
                            _print_question_with_marks(pdf, f"D] {clean_text(questions[5]['question'])}", 4, line_height)
                            pdf.ln(1)
                    
                    pdf.ln(6)
                    question_num += 1

        # Generate PDF based on exam type
        if examtype == 'insem':
            render_30_marks_pattern(pdf, unit_questions)
        elif examtype == 'endsem':
            render_60_marks_pattern_fixed(pdf, unit_questions)
        else:
            return "Invalid exam type", 400

        pdf_data = pdf.output(dest='S').encode('latin-1', errors='replace')
        pdf_buffer = io.BytesIO(pdf_data)
        pdf_buffer.seek(0)

        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name="Question_Paper.pdf",
            mimetype='application/pdf'
        )

    except Exception as e:
        print(f"ERROR: PDF generation error: {e}")
        return f"Error generating PDF: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)