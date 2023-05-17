from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import capfirst
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Q
from .models import Expense
from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from .models import Account




def index(request):

    return render(request,'index.html')

def register(request):
   
    if request.method=='POST':

        first_name=capfirst(request.POST['fname'])
        last_name=capfirst(request.POST['lname'])
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email1']
        phone = request.POST['phone']

      
        if password==cpassword:  #  password matching......
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                
                user.save()
                u = User.objects.get(id = user.id)

                company_details(contact_number = phone, user = u).save()
    
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('register')   
        return redirect('register')

    return render(request,'register.html')

def login(request):
        
    if request.method == 'POST':
        
        email_or_username = request.POST['emailorusername']
        password = request.POST['password']

        user = authenticate(request, username=email_or_username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('base')
        else:
            return redirect('/')

    return render(request, 'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def base(request):
   
    
    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'loginhome.html',context)

@login_required(login_url='login')
def view_profile(request):

    company = company_details.objects.get(user = request.user)
    context = {
                'company' : company
            }
    return render(request,'profile.html',context)

@login_required(login_url='login')
def edit_profile(request,pk):

    company = company_details.objects.get(id = pk)
    user1 = User.objects.get(id = company.user_id)

    if request.method == "POST":

        user1.first_name = capfirst(request.POST.get('f_name'))
        user1.last_name  = capfirst(request.POST.get('l_name'))
        user1.username = request.POST.get('uname')
        # pat.age = request.POST.get('age')
        # pat.address = capfirst(request.POST.get('address'))
        # pat.gender = request.POST.get('gender')
        # user1.email = request.POST.get('email')
        # pat.email = request.POST.get('email')
        # pat.contact_num = request.POST.get('cnum')
        # #fkey1= request.POST.get('doc')
        # #pat.doctor = doctor.objects.get(id = fkey1)
        # if len(request.FILES)!=0 :
        #     doc.profile_pic = request.FILES.get('file')


        company.save()
        user1.save()
        return redirect('view_profile')

    context = {
        'company' : company,
        'user1' : user1,
    }
    context = {
                'company' : company,
            }
    return render(request,'edit_profile.html',context)

@login_required(login_url='login')
def itemview(request):
    viewitem=AddItem.objects.all()
    return render(request,'item_view.html',{'view':viewitem})


@login_required(login_url='login')
def additem(request):
    unit=Unit.objects.all()
    sale=Sales.objects.all()
    purchase=Purchase.objects.all()
    
    


  
    
        



    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    

    return render(request,'additem.html',{'unit':unit,'sale':sale,'purchase':purchase,
               
                            "account":account,"account_type":account_type,"accounts":accounts,"account_types":account_types,
                            
                            })

@login_required(login_url='login')
def add_account(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']
       
        acc=Purchase(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()                 
        return redirect("additem")
        
    return render(request,'additem.html')


@login_required(login_url='login')
def add(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            radio=request.POST.get('radio')
            if radio=='tax':
    
                
                inter=request.POST['inter']
                intra=request.POST['intra']
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate=inter,intrastate=intra
                                )
                
            else:
                                                  
                type=request.POST.get('type')
                name=request.POST['name']
                unit=request.POST['unit']
                sel_price=request.POST.get('sel_price')
                sel_acc=request.POST.get('sel_acc')
                s_desc=request.POST.get('sel_desc')
                cost_price=request.POST.get('cost_price')
                cost_acc=request.POST.get('cost_acc')      
                p_desc=request.POST.get('cost_desc')
                u=request.user.id
                us=request.user
                history="Created by" + str(us)
                user=User.objects.get(id=u)
                unit=Unit.objects.get(id=unit)
                sel=Sales.objects.get(id=sel_acc)
                cost=Purchase.objects.get(id=cost_acc)
                ad_item=AddItem(type=type,Name=name,p_desc=p_desc,s_desc=s_desc,s_price=sel_price,p_price=cost_price,unit=unit,
                            sales=sel,purchase=cost,user=user,creat=history,interstate='none',intrastate='none'
                                )
                ad_item.save()
            ad_item.save()
           
            return redirect("itemview")
    return render(request,'additem.html')



@login_required(login_url='login')
def edititem(request,id):
    pedit=AddItem.objects.get(id=id)
    p=Purchase.objects.all()
    s=Sales.objects.all()
    u=Unit.objects.all()

    accounts = Purchase.objects.all()
    account_types = set(Purchase.objects.values_list('Account_type', flat=True))
    

    
    account = Sales.objects.all()
    account_type = set(Sales.objects.values_list('Account_type', flat=True))
    
    return render(request,'edititem.html',{"account":account,"account_type":account_type,'e':pedit,'p':p,'s':s,'u':u,"accounts":accounts,"account_types":account_types})


@login_required(login_url='login')
def edit_db(request,id):
        if request.method=='POST':
            edit=AddItem.objects.get(id=id)
            edit.type=request.POST.get('type')
            edit.Name=request.POST['name']
            unit=request.POST['unit']
            edit.s_price=request.POST['sel_price']
            sel_acc=request.POST['sel_acc']
            edit.s_desc=request.POST['sel_desc']
            edit.p_price=request.POST['cost_price']
            cost_acc=request.POST['cost_acc']        
            edit.p_desc=request.POST['cost_desc']
            
            
            edit.unit=Unit.objects.get(id=unit)
            edit.sales=Sales.objects.get(id=sel_acc)
            edit.purchase=Purchase.objects.get(id=cost_acc)
            edit.save()
            return redirect('itemview')

        return render(request,'edititem.html')


@login_required(login_url='login')
def detail(request,id):
    user_id=request.user
    items=AddItem.objects.all()
    product=AddItem.objects.get(id=id)
    history=History.objects.filter(p_id=product.id)
    print(product.id)
    
    
    context={
       "allproduct":items,
       "product":product,
       "history":history,
      
    }
    
    return render(request,'demo.html',context)


@login_required(login_url='login')
def Action(request,id):
    user=request.user.id
    user=User.objects.get(id=user)
    viewitem=AddItem.objects.all()
    event=AddItem.objects.get(id=id)
    

    print(user)
    if request.method=='POST':
        action=request.POST['action']
        event.satus=action
        event.save()
        if action == 'active':
            History(user=user,message="Item marked as Active ",p=event).save()
        else:
            History(user=user,message="Item marked as inActive",p=event).save()
    return render(request,'item_view.html',{'view':viewitem})

@login_required(login_url='login')
def cleer(request,id):
    dl=AddItem.objects.get(id=id)
    dl.delete()
    return redirect('itemview')


@login_required(login_url='login')
def add_unit(request):
    if request.method=='POST':
        unit_name=request.POST['unit_name']
        Unit(unit=unit_name).save()
        return redirect('additem')
    return render(request,"additem.html")


@login_required(login_url='login')
def add_sales(request):
    if request.method=='POST':
        Account_type  =request.POST['acc_type']
        Account_name =request.POST['acc_name']
        Acount_code =request.POST['acc_code']
        Account_desc =request.POST['acc_desc']        
        acc=Sales(Account_type=Account_type,Account_name=Account_name,Acount_code=Acount_code,Account_desc=Account_desc)
        acc.save()
        return redirect('additem')
    return render(request,'additem.html')

@login_required(login_url='login')
def recurringbase(request):
    expenses = Expense.objects.all()
    return render(request, 'recurring_base.html',{'expenses': expenses})

@login_required(login_url='login')
def recurringhome(request):
    selected_vendor_id = request.GET.get('vendor')
    vendors = vendor_table.objects.filter(user=request.user)
    selected_vendor = vendor_table.objects.filter(id=selected_vendor_id).first()
    gst_number = selected_vendor.gst_number if selected_vendor else ''
    return render(request, 'recurring_home.html', {
        'vendors': vendors,
        'selected_vendor_id': selected_vendor_id,
        'gst_number': gst_number,
    })




from django.shortcuts import get_object_or_404
from .models import Expense, vendor_table

def add_expense(request):
    if request.method == 'POST':
        profile_name = request.POST['profile_name']
        repeat_every = request.POST['repeat_every']
        start_date = request.POST['start_date']
        ends_on = request.POST['ends_on']
        expense_account = request.POST['expense_account']
        expense_type = request.POST['expense_type']
        goods_label = request.POST.get('goods_label')
        amount = request.POST['amount']
        currency = request.POST['currency']
        paidthrough = request.POST['paidthrough']
        vendor_id = request.POST['vendor']
        vendor = get_object_or_404(vendor_table, pk=vendor_id)
        gst = request.POST['gst']
        destination= request.POST['destination']
        tax= request.POST['tax']
        notes = request.POST['notes']
        customername= request.POST['customername']
        expense = Expense(profile_name=profile_name, repeat_every=repeat_every, start_date=start_date,
                          ends_on=ends_on, expense_account=expense_account, expense_type=expense_type,
                          goods_label=goods_label, amount=amount, currency=currency, paidthrough=paidthrough,
                          vendor=vendor, gst=gst,customername=customername,notes=notes,tax=tax,destination=destination)
        expense.save()
        return redirect('recurringbase')
    else:
        vendors = vendor_table.objects.all()
        return render(request, 'add_expense.html', {'vendors': vendors})



def show_recurring(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    
    return render(request, 'show_recurring.html', {'expense': expense})


def expense_details(request):
    expenses = Expense.objects.all()
    return render(request, 'recurring_base.html',{'expenses': expenses})

@login_required(login_url='login')
def vendor(request):
    return render(request,'create_vendor.html')



@login_required(login_url='login')
def add_vendor(request):
    if request.method=="POST":
        vendor_data=vendor_table()
        vendor_data.salutation=request.POST['salutation']
        vendor_data.first_name=request.POST['first_name']
        vendor_data.last_name=request.POST['last_name']
        vendor_data.company_name=request.POST['company_name']
        vendor_data.vendor_display_name=request.POST['v_display_name']
        vendor_data.vendor_email=request.POST['vendor_email']
        vendor_data.vendor_wphone=request.POST['w_phone']
        vendor_data.vendor_mphone=request.POST['m_phone']
        vendor_data.skype_number=request.POST['skype_number']
        vendor_data.designation=request.POST['designation']
        vendor_data.department=request.POST['department']
        vendor_data.website=request.POST['website']
        vendor_data.gst_treatment=request.POST['gst']

        x=request.POST['gst']
        if x=="Unregistered Business-not Registered under GST":
            vendor_data.pan_number=request.POST['pan_number']
            vendor_data.gst_number="null"
        else:
            vendor_data.gst_number=request.POST['gst_number']
            vendor_data.pan_number=request.POST['pan_number']

        vendor_data.source_supply=request.POST['source_supply']
        vendor_data.currency=request.POST['currency']
        vendor_data.opening_bal=request.POST['opening_bal']
        vendor_data.payment_terms=request.POST['payment_terms']

        user_id=request.user.id
        udata=User.objects.get(id=user_id)
        vendor_data.user=udata
        vendor_data.battention=request.POST['battention']
        vendor_data.bcountry=request.POST['bcountry']
        vendor_data.baddress=request.POST['baddress']
        vendor_data.bcity=request.POST['bcity']
        vendor_data.bstate=request.POST['bstate']
        vendor_data.bzip=request.POST['bzip']
        vendor_data.bphone=request.POST['bphone']
        vendor_data.bfax=request.POST['bfax']

        vendor_data.sattention=request.POST['sattention']
        vendor_data.scountry=request.POST['scountry']
        vendor_data.saddress=request.POST['saddress']
        vendor_data.scity=request.POST['scity']
        vendor_data.sstate=request.POST['sstate']
        vendor_data.szip=request.POST['szip']
        vendor_data.sphone=request.POST['sphone']
        vendor_data.sfax=request.POST['sfax']
        vendor_data.save()
# .......................................................adding to remaks table.....................
        vdata=vendor_table.objects.get(id=vendor_data.id)
        vendor=vdata
        rdata=remarks_table()
        rdata.remarks=request.POST['remark']
        rdata.user=udata
        rdata.vendor=vdata
        rdata.save()


#  ...........................adding multiple rows of table to model  ........................................................       
        salutation =request.POST.getlist('salutation[]')
        first_name =request.POST.getlist('first_name[]')
        last_name =request.POST.getlist('last_name[]')
        email =request.POST.getlist('email[]')
        work_phone =request.POST.getlist('wphone[]')
        mobile =request.POST.getlist('mobile[]')
        skype_number =request.POST.getlist('skype[]')
        designation =request.POST.getlist('designation[]')
        department =request.POST.getlist('department[]') 
        vdata=vendor_table.objects.get(id=vendor_data.id)
        vendor=vdata
       

        if len(salutation)==len(first_name)==len(last_name)==len(email)==len(work_phone)==len(mobile)==len(skype_number)==len(designation)==len(department):
            mapped2=zip(salutation,first_name,last_name,email,work_phone,mobile,skype_number,designation,department)
            mapped2=list(mapped2)
            print(mapped2)
            for ele in mapped2:
                created = contact_person_table.objects.get_or_create(salutation=ele[0],first_name=ele[1],last_name=ele[2],email=ele[3],
                         work_phone=ele[4],mobile=ele[5],skype_number=ele[6],designation=ele[7],department=ele[8],user=udata,vendor=vendor)
        
       
                 
        return redirect('recurringhome')
        
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    vendors = vendor_table.objects.all()


    if request.method == 'POST':
        expense.profile_name = request.POST.get('profile_name')
        expense.repeat_every = request.POST.get('repeat_every')
        expense.start_date = request.POST.get('start_date')
        expense.ends_on = request.POST.get('ends_on')
        expense.expense_account = request.POST.get('expense_account')
        expense.expense_type = request.POST.get('expense_type')
        expense.amount = request.POST.get('amount')
        expense.currency = request.POST.get('currency')
        expense.paidthrough = request.POST.get('paidthrough')
        expense.vendor_id = request.POST.get('vendor')
        expense.goods_label= request.POST.get('goods_label')
        expense.gst = request.POST.get('gst')
        expense.destination = request.POST.get('destination')
        expense.tax = request.POST.get('tax')
        expense.notes = request.POST.get('notes')
        expense.customername = request.POST.get('customername')

        expense.save()
        return redirect('recurringbase')

    else:
        return render(request, 'edit_expense.html', {'expense': expense, 'vendors': vendors})


@login_required(login_url='login')
def newexp(request):
    return render(request,'create_expense.html')


def save_data(request):
    if request.method == 'POST':
        account_type = request.POST.get('accountType')
        account_name = request.POST.get('accountName')
        account_code = request.POST.get('accountCode')
        description = request.POST.get('description')

        account = Account(accountType=account_type, accountName=account_name, accountCode=account_code, description=description)
        account.save()

        return redirect('recurringhome')

    return render(request, 'recurring_home.html')


from django.http import JsonResponse
from .models import Account

def get_account_names(request):
    account_names = Account.objects.values_list('accountName', flat=True)
    return JsonResponse(list(account_names), safe=False)


@login_required(login_url='login')
def profileshow(request):
    expenses = Expense.objects.all()
    return render(request, 'show_recurring.html', {'expenses': expenses})
