from django.shortcuts import render
from django.views.generic import TemplateView

"""
    --------------------------
    ---- Helper Functions ----
    --------------------------
"""
def scrapeMealData():
    mealData = {
        'breakfast': ['Scrambled Eggs', 'Hash Browns', 'Blueberry Pancakes'],
        'lunch': ['Pulled Pork', 'Ceasar Salad', 'French Fries'],
        'dinner': ['Roast Turkey', 'Mashed Potatoes', 'Pasta Alfredo']
    }
    #scrape meal data here
    return mealData


""" --- End Helper Functions --- """



# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class DetailPageView(TemplateView):
    def get(self, request, **kwargs):
        mealData = scrapeMealData()
        return render(request, 'detail.html', context={'breakfast': mealData['breakfast'],'lunch': mealData['lunch'],'dinner': mealData['dinner']})
