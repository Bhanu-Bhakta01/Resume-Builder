from django.shortcuts import render, redirect
from .models import PersonalInfo

def personal_info_view(request):
    if request.method == 'POST':
        # Get form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')
        portfolio = request.POST.get('portfolio')
        profile_summary = request.POST.get('profile_summary')

        # Save the data to the database
        PersonalInfo.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            address=address,
            linkedin=linkedin,
            github=github,
            portfolio=portfolio,
            profile_summary=profile_summary
        )
        return redirect('success')  # Redirect to a success page after saving

    return render(request, 'personal_info_form.html')
