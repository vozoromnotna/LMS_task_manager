from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import loader
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

#region FBV
def index(request):
    return render(request, 'quality_control/index.html')


def bugs(request):
    bugs_list =  get_list_or_404(BugReport)
    context = {'bugs_list': bugs_list}
    return render(request, 'quality_control/bugs_list.html', context)

def bug_details(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    context = {'bug': bug}
    return render(request, 'quality_control/bug_details.html', context)

def bug_add(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('quality_control:bugs'))
    else:   
        form = BugReportForm()
        
    context = {'form': form}
    return render(request, 'quality_control/bug_report_form.html', context)

def bug_update(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('quality_control:bug_details', kwargs={"bug_id": bug_id}))
    else:   
        form = BugReportForm(instance=bug)
    context = {'form': form}
    return render(request, 'quality_control/bug_update_form.html', context)

def bug_delete(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        bug.delete()
        return redirect(reverse_lazy('quality_control:bugs'))
    return render(request, 'quality_control/bug_delete.html', {'bug': bug})
        
        
def features(request):
    features_list =  get_list_or_404(FeatureRequest)
    context = {'features_list': features_list}
    return render(request, 'quality_control/features_list.html', context)

def feature_details(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    context = {'feature': feature}
    return render(request, 'quality_control/feature_details.html', context)

def feature_add(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('quality_control:features'))
    else:   
        form = FeatureRequestForm()
        
    context = {'form': form}
    return render(request, 'quality_control/feature_request_form.html', context)

def feature_update(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('quality_control:feature_details', kwargs={"feature_id": feature_id}))
    else:   
        form = FeatureRequestForm(instance=feature)
    context = {'form': form}
    return render(request, 'quality_control/feature_update_form.html', context)

def feature_delete(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        feature.delete()
        return redirect(reverse_lazy('quality_control:features'))
    return render(request, 'quality_control/feature_delete.html', {'feature': feature})

#endregion

#region CBV
class IndexView(TemplateView):
    template_name = 'quality_control/index.html'
    
    
class BugReportsListView(ListView):
    template_name = 'quality_control/bugs_list.html'
    model = BugReport
    context_object_name = 'bugs_list'


class BugReportView(DetailView):
    model = BugReport
    context_object_name = 'bug'
    pk_url_kwarg = 'bug_id'
    template_name='quality_control/bug_details.html'
    
class BugReportCreateView(CreateView):
    form_class = BugReportForm
    success_url = reverse_lazy('quality_control:bugs')
    template_name = 'quality_control/bug_report_form.html'
    
class BugReportUpdateView(UpdateView):
    form_class = BugReportForm
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_update_form.html'
    def get_success_url(self) -> str:
        return reverse('quality_control:bug_details', kwargs={'bug_id': self.kwargs['bug_id']})
    
class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_delete.html'
    success_url = reverse_lazy('quality_control:bugs')
    

class FeatureRequestsListView(ListView):
    template_name = 'quality_control/features_list.html'
    model = FeatureRequest
    context_object_name = 'features_list'
    

class FeatureRequestView(DetailView):
    model = FeatureRequest
    context_object_name = 'feature'
    pk_url_kwarg = 'feature_id'
    template_name='quality_control/feature_details.html'
    
class FeatureRequestCreateView(CreateView):
    form_class = FeatureRequestForm
    success_url = reverse_lazy('quality_control:features')
    template_name = 'quality_control/feature_request_form.html'
    
class FeatureRequestUpdateView(UpdateView):
    form_class = FeatureRequestForm
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_update_form.html'
    def get_success_url(self) -> str:
        return reverse('quality_control:feature_details', kwargs={'feature_id': self.kwargs['feature_id']})
    
class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_delete.html'
    success_url = reverse_lazy('quality_control:features')
#endregion
