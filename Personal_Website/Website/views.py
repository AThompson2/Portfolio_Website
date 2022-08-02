from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Website_steps, Website_content, steps2, content2

from django.conf import settings
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Create your views here.

class HomePage(TemplateView):
    template_name = 'Website/HomePage.html'

class AboutMe(TemplateView):
    template_name = 'Website/About_me.html'

# class ContactMe(TemplateView):
#     template_name = 'Website/ContactMe.html'

class TestPage(TemplateView):
    template_name = 'Website/TestPage.html'

class Test_js(TemplateView):
    template_name = 'Website/test_js.html'

class Portfolio_main(TemplateView):
    template_name = 'Website/Portfolio_main.html'


def ContactMe(request):
    if request.method == 'POST':
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
                email_message = form.cleaned_data['message']
                send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
                return render(request, 'Website/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'Website/ContactMe.html', context)


def successView(request):
    return HttpResponse('Thank you for your message, I will be in contact with you shortly.')

def Project1(request):
    step1 = Website_steps.objects.all().order_by('pk')
    A = Website_content.objects.get(pk=1)
    B = Website_content.objects.get(pk=2)
    C = Website_content.objects.get(pk=3)
    D = Website_content.objects.get(pk=4)
    E = Website_content.objects.get(pk=5)
    F = Website_content.objects.get(pk=6)
    G = Website_content.objects.get(pk=7)
    H = Website_content.objects.get(pk=8)
    I = Website_content.objects.get(pk=9)
    J = Website_content.objects.get(pk=10)
    K = Website_content.objects.get(pk=11)
    L = Website_content.objects.get(pk=12)
    M = Website_content.objects.get(pk=13)
    N = Website_content.objects.get(pk=14)
    O = Website_content.objects.get(pk=15)
    P = Website_content.objects.get(pk=16)
    Q = Website_content.objects.get(pk=17)
    R = Website_content.objects.get(pk=18)
    S = Website_content.objects.get(pk=19)
    T = Website_content.objects.get(pk=20)
    U = Website_content.objects.get(pk=21)
    V = Website_content.objects.get(pk=22)
    W = Website_content.objects.get(pk=23)
    X = Website_content.objects.get(pk=24)
    Y = Website_content.objects.get(pk=25)
    Z = Website_content.objects.get(pk=26)
    A1 = Website_content.objects.get(pk=27)
    B1 = Website_content.objects.get(pk=28)
    C1 = Website_content.objects.get(pk=29)
    D1 = Website_content.objects.get(pk=30)
    E1 = Website_content.objects.get(pk=31)
    F1 = Website_content.objects.get(pk=32)
    G1 = Website_content.objects.get(pk=33)
    H1 = Website_content.objects.get(pk=34)
    I1 = Website_content.objects.get(pk=35)
    J1 = Website_content.objects.get(pk=36)
    K1 = Website_content.objects.get(pk=37)
    L1 = Website_content.objects.get(pk=38)
    M1 = Website_content.objects.get(pk=39)
    N1 = Website_content.objects.get(pk=40)
    O1 = Website_content.objects.get(pk=41)
    P1 = Website_content.objects.get(pk=42)
    Q1 = Website_content.objects.get(pk=43)
    R1 = Website_content.objects.get(pk=44)
    S1 = Website_content.objects.get(pk=45)
    T1 = Website_content.objects.get(pk=46)
    U1 = Website_content.objects.get(pk=47)
    V1 = Website_content.objects.get(pk=48)
    W1 = Website_content.objects.get(pk=49)
    X1 = Website_content.objects.get(pk=50)
    Y1 = Website_content.objects.get(pk=51)
    Z1 = Website_content.objects.get(pk=52)
    A2 = Website_content.objects.get(pk=53)
    B2 = Website_content.objects.get(pk=54)
    C2 = Website_content.objects.get(pk=55)
    D2 = Website_content.objects.get(pk=56)
    E2 = Website_content.objects.get(pk=57)
    F2 = Website_content.objects.get(pk=58)
    G2 = Website_content.objects.get(pk=59)
    H2 = Website_content.objects.get(pk=60)
    I2 = Website_content.objects.get(pk=61)
    J2 = Website_content.objects.get(pk=62)
    K2 = Website_content.objects.get(pk=63)
    L2 = Website_content.objects.get(pk=64)
    M2 = Website_content.objects.get(pk=65)
    N2 = Website_content.objects.get(pk=66)
    O2 = Website_content.objects.get(pk=67)
    P2 = Website_content.objects.get(pk=68)
    Q2 = Website_content.objects.get(pk=69)
    R2 = Website_content.objects.get(pk=70)
    S2 = Website_content.objects.get(pk=71)
    T2 = Website_content.objects.get(pk=72)
    U2 = Website_content.objects.get(pk=73)

    AAA = Website_steps.objects.get(pk=1)
    BBB = Website_steps.objects.get(pk=2)
    CCC = Website_steps.objects.get(pk=3)
    DDD = Website_steps.objects.get(pk=4)
    EEE = Website_steps.objects.get(pk=5)
    FFF = Website_steps.objects.get(pk=6)
    GGG = Website_steps.objects.get(pk=7)
    HHH = Website_steps.objects.get(pk=8)
    III = Website_steps.objects.get(pk=9)
    JJJ = Website_steps.objects.get(pk=10)
    KKK = Website_steps.objects.get(pk=11)
    LLL = Website_steps.objects.get(pk=12)



    AA = A.website_steps_set.get()
    BB = B.website_steps_set.get()
    CC = C.website_steps_set.get()
    DD = D.website_steps_set.get()
    EE = E.website_steps_set.get()
    FF = F.website_steps_set.get()
    GG = G.website_steps_set.get()
    HH = H.website_steps_set.get()
    II = I.website_steps_set.get()
    JJ = J.website_steps_set.get()
    KK = K.website_steps_set.get()
    LL = L.website_steps_set.get()
    MM = M.website_steps_set.get()
    NN = N.website_steps_set.get()
    OO = O.website_steps_set.get()
    PP = P.website_steps_set.get()
    QQ = Q.website_steps_set.get()
    RR = R.website_steps_set.get()
    SS = S.website_steps_set.get()
    JJ1 = J1.website_steps_set.get()
    RR1 = R1.website_steps_set.get()
    VV1 = V1.website_steps_set.get()
    CC2 = C2.website_steps_set.get()
    GG2 = G2.website_steps_set.get()
    TT2 = T2.website_steps_set.get()


    content1 = AAA.website_cont.all().order_by('pk')
    content2 = BBB.website_cont.all().order_by('pk')
    content3 = CCC.website_cont.all().order_by('pk')
    content4 = DDD.website_cont.all().order_by('pk')
    content5 = EEE.website_cont.all().order_by('pk')
    content6 = FFF.website_cont.all().order_by('pk')
    content7 = GGG.website_cont.all().order_by('pk')
    content8 = HHH.website_cont.all().order_by('pk')
    content9 = III.website_cont.all().order_by('pk')
    content10 = JJJ.website_cont.all().order_by('pk')
    content11 = KKK.website_cont.all().order_by('pk')
    content12 = LLL.website_cont.all().order_by('pk')




    return render(request, 'Website/Project1.html', {
                                       'step1': step1,
                                       'content1': content1,
                                       'content2': content2,
                                       'content3': content3,
                                       'content4': content4,
                                       'content5': content5,
                                       'content6': content6,
                                       'content7': content7,
                                       'content8': content8,
                                       'content9': content9,
                                       'content10': content10,
                                       'content11': content11,
                                       'content12': content12,
                                       'AA': AA,
                                       'DD': DD,
                                       'GG': GG,
                                       'JJ': JJ,
                                       'OO': OO,
                                       'SS': SS,
                                       'JJ1': JJ1,
                                       'RR1': RR1,
                                       'VV1': VV1,
                                       'CC2': CC2,
                                       'GG2': GG2,
                                       'TT2': TT2,
                                        })


def Project2(request):
    step = steps2.objects.all().order_by('pk')

    A = content2.objects.get(pk=1)
    D = content2.objects.get(pk=4)
    H = content2.objects.get(pk=8)
    K = content2.objects.get(pk=11)
    N = content2.objects.get(pk=15)

    AA = A.steps2_set.get()
    DD = D.steps2_set.get()
    HH = H.steps2_set.get()
    KK = K.steps2_set.get()
    NN = N.steps2_set.get()

    AAA = steps2.objects.get(pk=1)
    BBB = steps2.objects.get(pk=2)
    CCC = steps2.objects.get(pk=3)
    DDD = steps2.objects.get(pk=4)
    EEE = steps2.objects.get(pk=5)

    content1 = AAA.website_cont2.all().order_by('pk')
    content21 = BBB.website_cont2.all().order_by('pk')
    content3 = CCC.website_cont2.all().order_by('pk')
    content4 = DDD.website_cont2.all().order_by('pk')
    content5 = EEE.website_cont2.all().order_by('pk')

    return render(request, 'Website/Project2.html',{
                                    'step': step,

                                    'content1': content1,
                                    'content21': content21,
                                    'content3': content3,
                                    'content4': content4,
                                    'content5': content5,

                                    'AA': AA,
                                    'DD': DD,
                                    'HH': HH,
                                    'KK': KK,
                                    'NN': NN,
                                        })
