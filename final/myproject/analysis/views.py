from django.shortcuts import render_to_response
from django.db.models import Count
from models import BusinessDetail


def month_wise_view(request):
    # month value from 01 to 12
    active_value_list = []
    for i in range(1, 13):
        value = BusinessDetail.objects.filter(current_period_started_at__month=i).filter(account_state='active').count()
        active_value_list.append(value)
    closed_value_list = []
    for i in range(1, 13):
        value = BusinessDetail.objects.filter(current_period_started_at__month=i).filter(account_state='closed').count()
        closed_value_list.append(value)    
  
    return render_to_response('monthly.html',{'active_value_list':active_value_list,'closed_value_list':closed_value_list})


def current_year_wise_active_account_record(request):
    #Bar chart
    total_active_count = BusinessDetail.objects.filter(current_period_started_at__year=2019).\
        filter(account_state='active').count()
    total_closed_count = BusinessDetail.objects.filter(current_period_started_at__year=2019).\
        filter(account_state='closed').count()
    return render_to_response('refe_pi.html', {'active': total_active_count,'closed':total_closed_count})


def account_state_category_wise(request):
    # stacked column chart
    category_account_list_active = BusinessDetail.objects.filter(account_state="active").values('parent_category_name').annotate(d_count = Count('parent_category_name'))   
    category_account_list_closed = BusinessDetail.objects.filter(account_state="closed").values('parent_category_name').annotate(d_count = Count('parent_category_name'))   
    
    parent_category_list = BusinessDetail.objects.values('parent_category_name')
    parent_category_list = [category.values()[0] for category in parent_category_list]
    parent_category_list = list(set(parent_category_list))
    
    # Active value added in list
    data = [(val['parent_category_name'], [val['d_count']]) for val in category_account_list_active]
    
    current_active_category = [val['parent_category_name'] for val in category_account_list_active]
    rem_category = set(parent_category_list) - set(current_active_category)
    for val in rem_category:
        data.append((val, [0]))
    
    # Closed value added in a list
    for cl_data in category_account_list_closed:
        for ac_data in data:
            if cl_data['parent_category_name'] == ac_data[0]:
                ac_data[1].append(cl_data['d_count'])
    # Single value case handled
    for value in data:
        if len(value[1]) != 2:
            value[1].append(0)
        
    # Fetch category id
    # category_id_mapping
    category_details = BusinessDetail.objects.all().values('parent_category_name', 'category_id').distinct()
    
    category_mapping = dict()
    for val in category_details:
        category_mapping[val['parent_category_name']] = val['category_id']
        
    # Three different list have to be made 
    category_list = [category_mapping[i[0]] for i in data]
    active_value_list = [i[1][0] for i in data]
    closed_value_list = [i[1][1] for i in data]
    return render_to_response('category_wise.html', {'category_list': category_list,
                                                     'active_value_list': active_value_list,
                                                     'closed_value_list': closed_value_list})


    
                                                                                                                                                                                                                                                                                                                                                                                                          


 


