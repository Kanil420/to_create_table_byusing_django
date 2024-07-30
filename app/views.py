from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q

def equi_joins(request):
    LEDO=Emp.objects.select_related('deptno').all()
    LEDO=Emp.objects.select_related('deptno').filter(ename='SMITH')
    LEDO=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    LEDO=Emp.objects.select_related('deptno').filter(sal__gte=10000)
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    LEDO=Emp.objects.select_related('deptno').filter(comm__gt=10)
    LEDO=Emp.objects.select_related('deptno').filter(comm__lt=10)
    LEDO=Emp.objects.select_related('deptno').filter(mgr=1111)



    d={'LEDO':LEDO}
    return render(request,'equi_joins.html',d)

def emp_db_mgr(request):
    EMO=Emp.objects.select_related('deptno','mgr').all()
    EMO=Emp.objects.select_related('deptno','mgr').filter(ename='SMITH')
    EMO=Emp.objects.select_related('deptno','mgr').filter(sal__gt=20)
    EMO=Emp.objects.select_related('deptno','mgr').filter(sal=44412,ename='SMITH')
    EMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    EMO=Emp.objects.select_related('deptno').filter(Q(ename='SMITH')& Q(sal__gt=5000)| Q(comm__lt=20))
    em

    
    


    d={'EMO':EMO}

    return render(request,'emp_db_mgr.html',d)