from django.http import HttpResponse
from django.shortcuts import render, redirect

from APP.models import *


def index(request):
    y = []
    select = request.POST.get('select')
    task = TaskTab.objects.all()
    task_partner = TaskPartnerTab.objects.all()
    if select == '我创建':
        for t in task:
            A = t.TCreate.UName == request.session.get('username')
            if A :
                x = []
                x.append(t.id)
                x.append(t.TName)
                x.append(t.TState)
                x.append(t.TPlanFinishTimestamp)
                x.append(t.TCreate.UName)
                x.append(t.TManager.UName)
                x.append({i.UserID.UName for i in task_partner if i.TaskID_id == t.id})
                y.append(x)
            a = 'checked'
        return render(request, 'index.html', {"list": y, "a": a})

    if select == '我负责的':
        for t in task:
            B = t.TManager.UName == request.session.get('username')
            if B:
                x = []
                x.append(t.id)
                x.append(t.TName)
                x.append(t.TState)
                x.append(t.TPlanFinishTimestamp)
                x.append(t.TCreate.UName)
                x.append(t.TManager.UName)
                x.append({i.UserID.UName for i in task_partner if i.TaskID_id == t.id})
                y.append(x)
            b = 'checked'
        return render(request, 'index.html', {"list": y, "b": b})

    if select == '我参与的':
        for t in task:
            C = request.session.get('username') in [i.UserID.UName for i in task_partner if i.TaskID_id == t.id]
            if C:
                x = []
                x.append(t.id)
                x.append(t.TName)
                x.append(t.TState)
                x.append(t.TPlanFinishTimestamp)
                x.append(t.TCreate.UName)
                x.append(t.TManager.UName)
                x.append({i.UserID.UName for i in task_partner if i.TaskID_id == t.id})
                y.append(x)
            c = 'checked'
        return render(request, 'index.html', {"list": y, "c": c})

    for t in task:
        print(t)
        A = t.TCreate.UName == request.session.get('username')
        B = t.TManager.UName == request.session.get('username')
        C = request.session.get('username') in [i.UserID.UName for i in task_partner if i.TaskID_id == t.id]
        print(A)
        print(B)
        print(C)
        print([i.UserID.UName for i in task_partner if i.TaskID_id == t.id])
        if A or B or C:
            x = []
            x.append(t.id)
            x.append(t.TName)
            x.append(t.TState)
            x.append(t.TPlanFinishTimestamp)
            x.append(t.TCreate.UName)
            x.append(t.TManager.UName)
            x.append({i.UserID.UName for i in task_partner if i.TaskID_id == t.id})
            y.append(x)
    d = 'checked'
    return render(request, 'index.html', {"list": y, "d": d})


def login(request):
    if request.method == 'POST':
        loginname = request.POST.get('loginname')
        password = request.POST.get('password')
        u = UserTab.objects.filter(LoginName=loginname).filter(LoginPassword=password).first()
        if u:
            request.session['is_login'] = True
            request.session['username'] = u.UName
            print(request.session.get('is_login'))
            print(request.session.get('username'))
            return redirect('index')
    return render(request, 'login.html')


def add(request):
    if request.method == 'POST':
        # sadf 2021-03-11 张三 ['张三', '李四']
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.getlist('d')

        e = request.POST.get('description')
        f = request.POST.get('grade')
        user1 = UserTab.objects.filter(UName=request.session.get('username')).first()
        user2 = UserTab.objects.filter(UName=c).first()
        t = TaskTab(TName=a, TState=1, TCreate=user1, TManager=user2, TPlanFinishTimestamp=b, TDescription=e, TGrade=f)
        t.save()
        for i in d:
            u = UserTab.objects.filter(UName=i).first()
            print(t)
            print(u)
            TaskPartnerTab.objects.create(TaskID=t, UserID=u)
        return redirect('index')
    return render(request, 'add.html')


def delete(request):
    if request.method=='POST':
        box_list = request.POST.getlist("checkboxBtn")
        for box in box_list:
            print(box)
            TaskTab.objects.filter(id=box).delete()
            TaskPartnerTab.objects.filter(TaskID=box).delete()
            return redirect('index')
    return HttpResponse('请求错误')


def detailed(request, id):
    task = TaskTab.objects.get(id=id)
    if request.method == 'POST':
        if task.TState == 1:
            task.TState = 0
        else:
            task.TState = 1
        task.save()
    task_partner = TaskPartnerTab.objects.filter(TaskID=id).all()
    tp = []
    for t_p in task_partner:
        tp.append(t_p.UserID.UName)
    return render(request, 'detailed.html', {'task': task, 'tp': tp})