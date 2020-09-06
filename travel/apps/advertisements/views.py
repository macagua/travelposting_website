from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
    View,
)
from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.urls import reverse_lazy
from apps.accounts.models import CustomerUser
from apps.utils.mixins  import NoCommunityRequiredMixin
from .models import (
    Advertiser,
    Category,
    Ad,
    AdImage
)
from .forms import (
    AdvertiserCreateForm,
    AdvertiserUpdateForm,
    CategoryCreateForm,
    CategoryUpdateForm,
    AdCreateForm,
    AdUpdateForm,
    AdImageCreateForm,
    AdImageUpdateForm
)


class AdvertisersListView(LoginRequiredMixin, ListView):
    ''' Advertisers List View '''
    template_name = 'advertisements/_advertisers_list.html'
    queryset = Advertiser.objects.all()

    def get_queryset(self):
        queryset = super(AdvertisersListView, self).get_queryset()
        return queryset.filter(created_by=self.request.user)


class AdvertiserCreateView(CreateView):
    ''' Advertiser Create View '''
    template_name = 'advertisements/_advertiser_create.html'
    form_class = AdvertiserCreateForm
    success_url = reverse_lazy('advertisements:advertisers-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['users_list'] = CustomerUser.objects.all().order_by('email')
        return c

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdvertiserUpdateView(UpdateView):
    ''' Advertiser Update View '''
    model = Advertiser
    form_class = AdvertiserUpdateForm
    template_name = 'advertisements/_advertiser_update.html'
    success_url = reverse_lazy('advertisements:advertisers-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['users_list'] = CustomerUser.objects.all().order_by('email')
        return c

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AdvertiserDeleteView(DeleteView):
    ''' Advertiser Delete View '''
    model = Advertiser
    # template_name = 'advertisements/_advertiser_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('advertisements:advertisers-list')


class CategoriesListView(LoginRequiredMixin, ListView):
    ''' Categories List View '''
    template_name = 'advertisements/_categories_list.html'
    queryset = Category.objects.all()

    def get_queryset(self):
        queryset = super(CategoriesListView, self).get_queryset()
        return queryset.filter(created_by=self.request.user)


class CategoryCreateView(CreateView):
    ''' Category Create View '''
    template_name = 'advertisements/_category_create.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('advertisements:categories-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['users_list'] = CustomerUser.objects.all().order_by('email')
        return c

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    ''' Category Update View '''
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'advertisements/_category_update.html'
    success_url = reverse_lazy('advertisements:categories-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['users_list'] = CustomerUser.objects.all().order_by('email')
        return c

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    ''' Category Delete View '''
    model = Category
    # template_name = 'advertisements/_category_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('advertisements:categories-list')


class AdsListView(LoginRequiredMixin, ListView):
    ''' Ads List View '''
    template_name = 'advertisements/_ads_list.html'
    queryset = Ad.objects.all()

    def get_queryset(self):
        queryset = super(AdsListView, self).get_queryset()
        return queryset.filter(created_by=self.request.user)


# class AdDetailView(NoCommunityRequiredMixin, DetailView):
#     template_name = 'advertisements/_ad_details.html'
#     queryset = Ad.objects.filter(id=self.request.id)


class AdCreateView(CreateView):
    ''' Ad Create View '''
    template_name = 'advertisements/_ad_create.html'
    form_class = AdCreateForm
    success_url = reverse_lazy('advertisements:ads-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['advertisers_list'] = Advertiser.objects.filter(created_by=self.request.user)
        c['categories_list'] = Category.objects.all()
        c['users_list'] = CustomerUser.objects.all().order_by('email')
        return c

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdUpdateView(UpdateView):
    ''' AdImage Update View '''
    model = Ad
    form_class = AdUpdateForm
    template_name = 'advertisements/_ad_update.html'
    success_url = reverse_lazy('advertisements:ads-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['advertisers_list'] = Advertiser.objects.filter(created_by=self.request.user)
        c['categories_list'] = Category.objects.all()
        c['users_list'] = CustomerUser.objects.all().order_by('email')
        return c

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AdDeleteView(NoCommunityRequiredMixin, DeleteView):
    ''' Ad Delete View '''
    model = Ad
    # template_name = 'advertisements/_ad_delete.html'

    # queryset = Ad.objects.filter(id=self.request.id)
    # success_url = reverse_lazy('advertisements:ads-list')
    
    def get_success_url(self):
        return reverse_lazy('advertisements:ads-list')

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)


class AdImagesListView(LoginRequiredMixin, ListView):
    ''' AdImages List View '''
    template_name = 'advertisements/_ad_images_list.html'
    queryset = AdImage.objects.all()

    def get_queryset(self):
        queryset = super(AdImagesListView, self).get_queryset()
        return queryset


class AdImageCreateView(CreateView):
    ''' AdImage Create View '''
    template_name = 'advertisements/_ad_image_create.html'
    form_class = AdImageCreateForm
    success_url = reverse_lazy('advertisements:ad-images-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['ads_list'] = Ad.objects.all()
        return c

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class AdImageUpdateView(UpdateView):
    ''' AdImage Update View '''
    model = AdImage
    form_class = AdImageUpdateForm
    template_name = 'advertisements/_ad_image_update.html'
    success_url = reverse_lazy('advertisements:ad-images-list')

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['ads_list'] = Ad.objects.all()
        return c

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AdImageDeleteView(DeleteView):
    ''' AdImage Delete View '''
    model = AdImage
    # template_name = 'advertisements/_ad_image_delete.html'

    def get_success_url(self):
        return reverse_lazy('advertisements:ad-images-list')
