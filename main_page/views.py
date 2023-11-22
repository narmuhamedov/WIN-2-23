from django.shortcuts import render, get_object_or_404
from .models import RunString, FilmPostModel, Afisha, Slider


def string_post_view(request):
    if request.method == 'GET':
        string_ = RunString.objects.all()
        film_list = FilmPostModel.objects.all()
        afisha = Afisha.objects.all()
        slider = Slider.objects.all()
        return render(request, template_name='main_page/index.html',
                      context={
                          'string_': string_,
                          'film_list': film_list,
                          'afisha': afisha,
                          'slider_list': slider

                      })


def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(FilmPostModel, id=id)
        return render(request, template_name='main_page/film_detail.html', context={'film_id': film_id})
