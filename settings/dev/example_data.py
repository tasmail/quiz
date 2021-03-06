# -*- coding: utf-8 -*-
from settings.base import *

API['disable_cors'] = True

DATABASE['data'] = {
    'users': [
        {
            'login': 'admin',
            'password': 'admin',
            'is_admin': True
        },
        {
            'login': 'user1',
            'password': 'user1',
            'is_admin': False
        },
    ],
    'quiz-categories': [
        {
            'name': 'Category 1',
            'comments': 'Some comments on Category 1',
        },
        {
            'name': 'Category 2',
            'comments': 'Some comments on Category 2',
        },
    ],
    'quizzes': [
        {
            'name': 'Test 1',
            'category_id': 1,
            'comments': 'Some comments on quiz Test 1',
        },
        {
            'name': 'Test 2',
            'category_id': 2,
            'comments': 'Some comments on quiz Test 2',
        },
    ],
    'questions': [
        {
            'question': 'Question 1',
            'quiz_id': 1
        },
        {
            'question': 'Question 2',
            'quiz_id': 1
        },
        {
            'question': 'Question 3',
            'quiz_id': 1
        },
        {
            'question': 'Question 1',
            'quiz_id': 2
        },
        {
            'question': 'Question 2',
            'quiz_id': 2
        },
    ],
    'question-choices': [
        {
            'choice': 'Question Choice 1',
            'question_id': 1
        },
        {
            'choice': 'Question Choice 2',
            'question_id': 1
        },
        {
            'choice': 'Question Choice 3',
            'question_id': 1,
            'is_right': True
        },
        {
            'choice': 'Question Choice 1',
            'question_id': 2
        },
        {
            'choice': 'Question Choice 2',
            'question_id': 2,
            'is_right': True
        },
        {
            'choice': 'Question Choice 3',
            'question_id': 2,
        },
        {
            'choice': 'Question Choice 1',
            'question_id': 3,
            'is_right': True
        },
        {
            'choice': 'Question Choice 2',
            'question_id': 3,
        },
        {
            'choice': 'Question Choice 3',
            'question_id': 3,
        },
        {
            'choice': 'Question Choice 1',
            'question_id': 4,
            'is_right': True
        },
        {
            'choice': 'Question Choice 2',
            'question_id': 4,
        },
        {
            'choice': 'Question Choice 3',
            'question_id': 4,
        },
        {
            'choice': 'Question Choice 1',
            'question_id': 5,
        },
        {
            'choice': 'Question Choice 2',
            'question_id': 5,
        },
        {
            'choice': 'Question Choice 3',
            'question_id': 5,
            'is_right': True
        },
    ],
}
