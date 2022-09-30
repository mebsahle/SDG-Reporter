#  import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
#  import redirect, reverse, reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# import templateview
from django.views.generic import TemplateView
# import genericview
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Country, Goal, Indicator, Performance

from datetime import datetime


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'

    goals = [
        {
            'pk': 1,
            'name': 'SDG 1: No Poverty',
            'description': 'No poverty means that every person in the world has access to basic needs.',
            'image': '../static/assets/img/goals/1.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/no-poverty/'
        },
        {
            'pk': 2,
            'name': 'SDG 2: Zero Hunger',
            'description': 'Zero hunger means that all people have access to enough food to meet their basic needs.',
            'image': '../static/assets/img/goals/2.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/zero-hunger/'
        },
        {
            'pk': 3,
            'name': 'SDG 3: Good Health and Well-being',
            'description': 'Good health means that every person in the world has access to safe, quality, and affordable health care.',
            'image': '../static/assets/img/goals/3.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/good-health-and-well-being/'
        },
        {
            'pk': 4,
            'name': 'SDG 4: Quality Education',
            'description': 'Quality education means that every person in the world has access to education that is free of charge and accessible to all.',
            'image': '../static/assets/img/goals/4.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/quality-education/'
        },
        {
            'pk': 5,
            'name': 'SDG 5: Gender Equality',
            'description': '',
            'image': '../static/assets/img/goals/5.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 6,
            'name': 'SDG 6: Clean Water and Sanitation',
            'description': '',
            'image': '../static/assets/img/goals/6.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 7,
            'name': 'SDG 7: Affordable and Clean Energy',
            'description': '',
            'image': '../static/assets/img/goals/7.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 8,
            'name': 'SDG 8: Decent Work and Economic Growth',
            'description': '',
            'image': '../static/assets/img/goals/8.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 9,
            'name': 'SDG 9: Industry, Innovation and Infrastructure',
            'description': '',
            'image': '../static/assets/img/goals/9.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 10,
            'name': 'SDG 10: Reduced Inequality',
            'description': '',
            'image': '../static/assets/img/goals/10.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 11,
            'name': 'SDG 11: Sustainable Cities and Communities',
            'description': '',
            'image': '../static/assets/img/goals/11.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 12,
            'name': 'SDG 12: Responsible Consumption and Production',
            'description': '',
            'image': '../static/assets/img/goals/12.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 13,
            'name': 'SDG 13: Climate Action',
            'description': '',
            'image': '../static/assets/img/goals/13.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 14,
            'name': 'SDG 14: Life Below Water',
            'description': '',
            'image': '../static/assets/img/goals/14.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 15,
            'name': 'SDG 15: Life On Land',
            'description': '',
            'image': '../static/assets/img/goals/15.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 16,
            'name': 'SDG 16: Peace, Justice and Strong Institutions',
            'description': '',
            'image': '../static/assets/img/goals/16.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'pk': 17,
            'name': 'SDG 17: Partnerships for the Goals',
            'description': '',
            'image': '../static/assets/img/goals/17.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        }
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        # get the first country in the list
        context['country'] = Country.objects.first()
        # add the  17 SDG goals to the context dictionary
        context['goals'] = self.goals
        return context

    # create country objects from the foem and save to database
    def post(self, request, *args, **kwargs):
        country = Country()
        # print("request post", request.POST['country_name'])
        # 1/0
        country.country_name = request.POST['country_name']
        country.flag = request.FILES['flag']
        country.recorded_by = request.user
        country.save()
        print(request.POST)
        return redirect('home')


class GoalDetailView(LoginRequiredMixin, TemplateView):
    model = Goal
    template_name = 'home/goal-detail.html'

    goals = [
        {
            'id': 1,
            'name': 'SDG 1: No Poverty',
            'description': 'No poverty means that every person in the world has access to basic needs.',
            'image': '../static/assets/img/goals/1.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/no-poverty/'
        },
        {
            'id': 2,
            'name': 'SDG 2: Zero Hunger',
            'description': 'Zero hunger means that all people have access to enough food to meet their basic needs.',
            'image': '../static/assets/img/goals/2.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/zero-hunger/'
        },
        {
            'id': 3,
            'name': 'SDG 3: Good Health and Well-being',
            'description': 'Good health means that every person in the world has access to safe, quality, and affordable health care.',
            'image': '../static/assets/img/goals/3.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/good-health-and-well-being/'
        },
        {
            'id': 4,
            'name': 'SDG 4: Quality Education',
            'description': 'Quality education means that every person in the world has access to education that is free of charge and accessible to all.',
            'image': '../static/assets/img/goals/4.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/quality-education/'
        },
        {
            'id': 5,
            'name': 'SDG 5: Gender Equality',
            'description': '',
            'image': '../static/assets/img/goals/5.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 6,
            'name': 'SDG 6: Clean Water and Sanitation',
            'description': '',
            'image': '../static/assets/img/goals/6.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 7,
            'name': 'SDG 7: Affordable and Clean Energy',
            'description': '',
            'image': '../static/assets/img/goals/7.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 8,
            'name': 'SDG 8: Decent Work and Economic Growth',
            'description': '',
            'image': '../static/assets/img/goals/8.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 9,
            'name': 'SDG 9: Industry, Innovation and Infrastructure',
            'description': '',
            'image': '../static/assets/img/goals/9.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 10,
            'name': 'SDG 10: Reduced Inequality',
            'description': '',
            'image': '../static/assets/img/goals/10.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 11,
            'name': 'SDG 11: Sustainable Cities and Communities',
            'description': '',
            'image': '../static/assets/img/goals/11.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 12,
            'name': 'SDG 12: Responsible Consumption and Production',
            'description': '',
            'image': '../static/assets/img/goals/12.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 13,
            'name': 'SDG 13: Climate Action',
            'description': '',
            'image': '../static/assets/img/goals/13.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 14,
            'name': 'SDG 14: Life Below Water',
            'description': '',
            'image': '../static/assets/img/goals/14.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 15,
            'name': 'SDG 15: Life On Land',
            'description': '',
            'image': '../static/assets/img/goals/15.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 16,
            'name': 'SDG 16: Peace, Justice and Strong Institutions',
            'description': '',
            'image': '../static/assets/img/goals/16.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        },
        {
            'id': 17,
            'name': 'SDG 17: Partnerships for the Goals',
            'description': '',
            'image': '../static/assets/img/goals/17.png',
            'url': 'https://www.un.org/en/development-assessment/indicators/'
        }
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Goal Detail'
        context['country'] = Country.objects.first()
        # get the url
        url = self.request.path
        # print("url", self.goals)
        # get the id from the url
        id = url.split('/')[-2]
        # print("id", id)
        # get the goal from the id
        goal = [goal for goal in self.goals if goal['id'] == int(id)][0]
        print("goal", goal, self.kwargs['pk'])
        context['sdg'] = goal
        context['indicators'] = Indicator.objects.filter(indicator_goal=Goal.objects.get(goal_number=self.kwargs['pk']))
        print('indicator', context['indicators'])
        return context


class PerformanceDetailView(LoginRequiredMixin, DetailView):
    model = Indicator
    template_name = 'home/performance_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs['pk']
        context['title'] = 'Performance Detail'
        context['country'] = Country.objects.first()
        print(self.kwargs['pk'], self.request.path)
        goal_number = self.request.path.split('/')[-3]
        
        print("id", self.kwargs['pk'])
        # check if performance exists
        if Performance.objects.filter(indicator_id=Indicator.objects.get(id=self.kwargs['pk'])).exists():
            context['performance_all'] = Performance.objects.filter(indicator_id=Indicator.objects.get(id=self.kwargs['pk']))
            context['indicators'] = Indicator.objects.get(id=self.kwargs['pk'])
            print("indicators in PDV", context['indicators'])
            context['performance'] = Performance.objects.filter(indicator_id__id=self.kwargs['pk']).last()
        
            # get list of years
            years = []
            for performance in Performance.objects.filter(indicator_id__id=self.kwargs['pk']):
                years.append(performance.year)
            print("years", years)
            context['years'] = years

            # get list of values
            values = []
            for performance in Performance.objects.filter(indicator_id__id=self.kwargs['pk']):
                values.append(performance.value)
            context['values'] = values
            # print("P_ALL",list(Performance.objects.filter(indicator_id=Indicator.objects.get(id=self.kwargs['pk']))))
            performance_all = list(Performance.objects.filter(indicator_id=Indicator.objects.get(id=self.kwargs['pk'])))

            # trend
            if len(performance_all) > 1:
                context['trend'] = performance_all[-1].value - performance_all[-2].value
            context['trend'] = performance_all[-1].value
            print("TREND", context['trend'])
        else:
            context['performance'] = []
        return context


class PerformanceCreateView(LoginRequiredMixin, TemplateView):
    model = Performance
    template_name = 'home/performance_create.html'

    def get_context_data(self, **kwargs):
        url = self.request.path
        id = url.split('/')[-2]
        print("id", id)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Performance Create'
        context['country'] = Country.objects.first()
        context['indicator'] = Indicator.objects.get(id=id)
        p_year = [int(i) for i in range(datetime.now().year, 2015-1, -1)]
        context['years'] = p_year
        return context
    
    def post(self, request, *args, **kwargs):
        url = self.request.path
        id = url.split('/')[-2]
        print("id", id)
        indicator = Indicator.objects.get(id=id)
        year = request.POST.get('year')
        value = request.POST.get('value')
        reference = request.POST.get('reference')
        source = request.POST.get('source')
        print("year", year)
        print("value", value)
        print("indicator", indicator)
        # prnt(indicator.)
        performance = Performance.objects.create(
            indicator_id=indicator,
            year=year,
            value=value,
            reference=reference,
            source=source,
            recorded_by=request.user
        )
        print("performance", performance)
        return redirect('performance_detail', id=indicator.indicator_goal.id, pk=id)