from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from phonereviewsapp.models import Phone, Store, PhoneReview
from phonereviewsapp.forms import PhoneForm, StoreForm


class PhoneDetail(DetailView):
    model = Phone
    template_name = 'phonereviewsapp/phone_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PhoneDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = PhoneReview.RATING_CHOICES
        return context


class PhoneCreate(CreateView):
    model = Phone
    template_name = 'phonereviewsapp/phone_form.html'
    form_class = PhoneForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PhoneCreate, self).form_valid(form)


class PhoneEdit(UpdateView):
    model = Phone
    template_name = 'phonereviewsapp/phone_edit_form.html'
    form_class = PhoneForm

    def form_valid(self, form):
        redirect = self.request.GET.get('next')
        if redirect:
            self.success_url = redirect
        return super(PhoneEdit, self).form_valid(form)


class StoreCreate(CreateView):
    model = Store
    template_name = 'phonereviewsapp/store_form.html'
    form_class = StoreForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.phone = Phone.objects.get(id=self.kwargs['pk'])

        redirect = self.request.GET.get('next')
        if redirect:
            self.success_url = redirect
        return super(StoreCreate, self).form_valid(form)


class StoreEdit(UpdateView):
    model = Store
    template_name = 'phonereviewsapp/store_edit_form.html'
    form_class = StoreForm

    def form_valid(self, form):

        redirect = self.request.GET.get('next')
        if redirect:
            self.success_url = redirect
        return super(StoreEdit, self).form_valid(form)


def review_create(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    review = PhoneReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        phone=phone)
    review.save()
    return HttpResponseRedirect(reverse('phonereviewsapp:phone_detail', args=(phone.id,)))


def review_delete(request, pk):
    review = get_object_or_404(PhoneReview, pk=pk)

    if request.method == 'POST':
        review.delete()

    return HttpResponseRedirect(reverse('phonereviewsapp:phone_detail', args=(review.phone.id,)))


def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)

    if request.method == 'POST':
        store.delete()

    return HttpResponseRedirect(reverse('phonereviewsapp:phone_detail', args=(store.phone.id,)))


def phone_delete(request, pk):
    phone = get_object_or_404(Phone, pk=pk)

    if request.method == 'POST':
        phone.delete()

    return HttpResponseRedirect(reverse('phonereviewsapp:phone_list'))
