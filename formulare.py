from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange

class RegistracniFormular(FlaskForm):
    jmeno = StringField('Jméno',
                        validators=[DataRequired(), Length(min=2, max=20)])
    prijmeni = StringField('Příjmení',
                        validators=[DataRequired(), Length(min=2, max=20)])
    vek = IntegerField('Věk',
                        validators=[DataRequired(), NumberRange(min=18)])
    email = StringField('Email',
                        validators=[DataRequired()])  #jeste validator na email
    telefon = IntegerField('Telefon',
                        validators=[DataRequired()])
    ulice = StringField('Ulice',
                        validators=[DataRequired()])
    mesto = StringField('Město',
                        validators=[DataRequired(), Length(min=2, max=20)])
    psc = StringField('PSČ',
                        validators=[DataRequired()])
    
    potvrdit = SubmitField('Registrace')
    
class VyhledavaciFormular(FlaskForm):
    jmeno = StringField('Jméno',
                        validators=[DataRequired(), Length(min=2, max=20)])
    prijmeni = StringField('Příjmení',
                        validators=[DataRequired(), Length(min=2, max=20)])
    potvrdit = SubmitField('Vyhledání')
    
    
class EditujFormular(FlaskForm):
    jmeno = StringField('Jméno',
                        validators=[DataRequired(), Length(min=2, max=20)])
    prijmeni = StringField('Příjmení',
                        validators=[DataRequired(), Length(min=2, max=20)])
    udaj = SelectField('Údaj',
                        choices=[("Email" ,"Email"), ("Telefon", "Telefon"), ("Ulice_ČP", "Ulice_ČP"), ("Město", "Město"), ("PSČ", "PSČ")])
    hodnota = StringField('Hodnota',
                        validators=[DataRequired(), Length(min=2, max=50)])
    
    potvrdit = SubmitField('Editace')
    
    
    
    
    
