# -*- coding: utf-8 -*-

def index():
    form = FORM(INPUT(_name='firstname'),
                INPUT(_name='lastname'),
                INPUT(_name='date_of_birth'),
                INPUT(_name='zipcode'),
                BUTTON('This is a button, is it not?', _type='submit'),
                _action="save_info",
               )
    form = SQLFORM.factory(Field(
                               'firstname',
                               label='What should we call you?',
                               requires=IS_NOT_EMPTY(),
                           ),
                           Field(
                               'lastname',
                               label='What is your family name?',
                               requires=IS_NOT_EMPTY(),
                           ),
                           Field(
                               'date_of_birth',
                               label='Date of Birth',
                               requires=IS_NOT_EMPTY(),
                           ),
                           Field(
                               'zipcode',
                               label='Zipcode',
                               requires=IS_NOT_EMPTY(),
                           ),
    )
    if form.process():
        print(form.vars)
    return dict(message='Cool', form=form)
