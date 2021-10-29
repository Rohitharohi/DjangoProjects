from django.shortcuts import render
from converter import forms

# Create your views here

def word_converter(request):
    if request.method=="get":

        form=forms.Converter()
        context={"form":form}

    if request.method=="post":
        form=forms.Converter(request.POST)
        if form.is_valid():
            single_digits = ["zero", "one", "two", "three",
                             "four", "five", "six", "seven",
                             "eight", "nine"]
            two_digits = ["", "ten", "eleven", "twelve",
                          "thirteen", "fourteen", "fifteen",
                          "sixteen", "seventeen", "eighteen",
                          "nineteen"]
            tens_multiple = ["", "", "twenty", "thirty", "forty",
                             "fifty", "sixty", "seventy", "eighty",
                             "ninety"]

            tens_power = ["hundred", "thousand"]
    return render(request,"word.html",context)
