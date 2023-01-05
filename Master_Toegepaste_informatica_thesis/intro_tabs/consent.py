from app import app 
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc


layout = html.Div([
    html.H3('Geïnformeerde toestemming/Informed consent',id="consent_title"),
   
    html.Div([
        html.Div([
        html.P("Titel van het onderzoek/Title of the study:",className="consent_p"),
        html.P("Master's thesis-Visualization of wine reviews"),
        html.P("Naam en contactgegevens van onderzoekers/Researcher's name and contact info:",className="consent_p"),
        html.P("Promotor: Katrien Verbert-katrien.verbert@cs.kuleuven.be",className="consent_p_answers"),
        html.P("Student: Serhat Erdogan-serhat.erdogan@student.kuleuven.be"),
        html.P("Doel en methodologie van het onderzoek/Goal and methodology of the study",className="consent_p"),
        html.P("Het visualizeren en evalueren van wine reviews.",className="consent_p_answers"),
        html.P("Visualizing and evaluation of wine reviews.",className="consent_english"),
        html.P("Duur van het experiment/Experiment duration:",className="consent_p"),
        html.P("+-25 min"),
        ],id="div_in_card"),
    ],id="consent_form_card"),

    html.Ul([
        html.Li(["Ik begrijp dat mijn deelname aan deze studie vrijwillig is. Ik heb het recht om mijn deelname op elk moment stop te zetten.",html.Br()," Daarvoor hoef ik geen reden te geven en ik weet dat daaruit geen nadeel voor mij kan ontstaan."
        ,html.Br(),html.Span("I understand that participation in this study is voluntary. I have the right to end my participation at any given time. I do not need to provide any reason for this and know that it will not lead to any negative consequences for myself.",className="consent_english")]),
        
        html.Li(["Ik weet dat ik zal deelnemen aan volgende proeven of testen:",html.Br(),
        html.Span("I am aware that i will participate in the following tests or experiments:",className="consent_english"),
            html.Ul([
                html.Li(["Ik zal gevraagd worden het ontwikkelde systeem te bekijken en/of gebruiken, in vrije verkenning of met specifiek opdracht.",
                html.Br(),html.Span("I will be asked to view and/or use the developed system freely or given a specific task.",className="consent_english")]),

                html.Li(["Tijdens mijn interactie met het systeem kunnen logs van mijn interactie (zoals gekozen wijn attributes/wijn namen) opgeslagen worden, alsook info ivm tijdsduur voor bepaalde interacties of gebruikerstaken.",
                html.Br(),html.Span("During my interactions with the system, logs of my different interactions (such as the chosen wine attributes/wine names) will be saved, as well as various timings regarding certain interactions or user tasks",className="consent_english")]),

                html.Li(["Ik kan gevraagd worden mijn gedacht en bedoeling tijdesn het bekijken of gebruiken van het systeem luidop te delen",
                html.Br(),html.Span("I can be asked to share my thoughts and intentions while viewing or using the system aloud",className="consent_english")]),

                html.Li(["Ik kan voor het gebruik van het systeem vragen gesteld worden in verband met demografische gegevens, mijn persoonlijkheid en mijn voorkeuren naar wijnen. Ik behoud de vrijheid om een vraag niet te beantwoorden en hoer daarvoor geen reden te geven.",
                html.Br(),html.Span("Before using the system, I can be asked questions about demographic data, my personality and my wine preferences. I keep the freedom not to answer a question and not give a reason for it.",className="consent_english")]),

                html.Li(["Het resultaat van deze studie kan worden gepubliceerd. Mijn naam wordt niet opgenomen in de publicatie, anonimiteit en de privacy van de gegevens is gegarandeerd in elke fase van het onderzoek.",
                html.Br(),html.Span("The result of this study can be be published. My name will not be included in the publication, anonymity and the privacy of the data is guaranteed in every stage of the study.",className="consent_english")]),
                    
            ],id="consent_list2"),
            ]),
            
         html.Li(["Voor vragen weet ik na mijn deelname terecht kan bij:",
         html.Br(),html.Span("For questions after my participation I know i can contact:",className="consent_english"),html.Br(),html.Span("Serhat Erdogan-serhat.erdogan@student.kuleuven.be",id="consent_name")]),
         
         html.Li(["Voor eventuele klachten of andere bezorgdheden omtrent ethische aspecten van deze studie kan ik contact opnemen met de Sociaal-Maatschappelijke Ethische Commissie van KU Leuven:",
         html.Br(),html.Span("For any complaints or other concers regarding the ethical aspects of this study I can contact the Social and Societal Ethics Committee of KU Leuven",className="consent_english"),html.Br(),html.Span("smec@kuleuven.be",id="consent_name")]),
        
        ],id="consent_list"),

        dcc.Checklist(id='consent_agree_check'
        , options = [
            {'label':'Ik heb bovestaand informatie gelezen en begrepen en heb antwoord gekregen op al mijn vragen betreffende deze studie. Ik stem toe om deel te nemen.', 'value':'agree'}
        ],),

        html.Span("I have read and comprehended the preceding information and had all of my questions regarding this study answered. I agree to participate.",className="consent_english"),
    
    dcc.Link("Next", href='/',id="consent_button",)

],id="mainConsent")



@app.callback(Output('consent_button', 'href'),
              [Input('consent_agree_check', 'value')])
def unlock_button(value):
    if value is None:
        return '/'
    if len(value)== 0:
        return '/'
    if value[0] == "agree":
        return '/tutorial'
