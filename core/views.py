from django.shortcuts import render, redirect
import pickle
import sklearn
import numpy as np


# Create your views here.


def index(request):
    return render(request, 'index.html')


def WinePredict(request):
    if request.method == "POST":
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cp = request.POST.get('cp')
        rbp = request.POST.get('rbp')
        chol = request.POST.get('chol')

        rest = request.POST.get('rest')
        mhr = request.POST.get('mhr')
        eia = request.POST.get('eia')
        st = request.POST.get('st')
        slope = request.POST.get('slope')

        major = request.POST.get('major')
        thala = request.POST.get('thala')
        try:

            with open('sc.obj', "rb") as f:
                sc = pickle.load(f)

            with open('model.obj', "rb") as f:
                model = pickle.load(f)

            print(int(age), int(cp), float(rbp), float(chol), int(
                rest), float(mhr), int(eia), float(st), int(slope), int(major), int(thala),  float(gender))

            x = np.array([int(age), int(cp), float(rbp), float(chol), int(
                rest), float(mhr), int(eia), float(st), int(slope), int(major), int(thala), float(gender)])

            x = x.reshape(1, -1)

            x = sc.fit_transform(x)
            print(x)
            output = model.predict(x)
            print(output)
        except Exception as e:
            print(e)
            print("something went wrong")

        res = ''
        if output[0] == 0:
            res = 'No Disease'
        else:
            res = 'You Have Disease'

        print(res)
        context = {
            'data': output[0],
            'q': res,
        }
        return render(request, 'output.html', context)

    return render(request, 'predict.html')


def Output(request):
    return render(request, 'output.html')
