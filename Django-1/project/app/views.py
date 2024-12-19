from django.shortcuts import render , get_object_or_404
from .models import Question, Answer


def homepage(request):
    return render(request, "homepage.html")

def questions_page(request):
    questions = Question.objects.all()
    results = None

    if request.method == 'POST':
        selected_answers = request.POST
        results = []

        for question in questions:
            selected_answer_id = selected_answers.get(f'question_{question.id}')
            selected_answer = None
            is_correct = False

            if selected_answer_id:
                selected_answer = question.answer_set.filter(id=selected_answer_id).first()
                is_correct = selected_answer.is_correct if selected_answer else False
            
            results.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': is_correct,
                'correct_answers': question.answer_set.filter(is_correct=True),
            })
    
    return render(request, 'questions.html', {'questions': questions, 'results': results})




