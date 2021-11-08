from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import ToDoList, Item
from . forms import CreateNewList
# from . forms import UpdateForm

# Create your views here.

def delete(request, pk):
		task = ToDoList.objects.get(id=pk)
		if request.method == "POST":
			task.delete()
			return HttpResponseRedirect("/view/")
				
		context = {"t":task}
		return render(request, "main/delete.html", context)

def index(response, id):
	ls = ToDoList.objects.get(id=id)

	if ls in response.user.todolist.all():

		#custom form
		if response.method == "POST":
			print(response.POST)
			if response.POST.get("save"):
				for item in ls.item_set.all():
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else:
						item.complete = False
					item.save()

			elif response.POST.get("newItem"):
				txt = response.POST.get("new")

				if len(txt) > 2:
					ls.item_set.create(text=txt, complete=False)
				else:
					print("invalid")

		return render(response, "main/list.html", {"ls":ls})
	return render(response, "main/view.html", {})


def home(response):
	return render(response, "main/home.html", {})

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()


	return render(response, "main/create.html", {"form":form})

def view(response):
	return render(response, "main/view.html", {})

def updateTask(request, pk):
	task = ToDoList.objects.get(id=pk)
	form = UpdateForm(instance=task)

	if response.method == "POST":
			form = UpdateForm(response.POST, instance=task)

	if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)

		
	context = {"form":form}
	return render(request, "main/create.html", context)

	# def update(request, pk):

	# 	task = ToDoList.objects.get(id=pk)
	# 	form = CreateNewList(instance=task)

	# 	if response.method == "POST":
	# 		form = CreateNewList(response.POST, instance=task)

	# 	if form.is_valid():
	# 		n = form.cleaned_data["name"]
	# 		t = ToDoList(name=n)
	# 		t.save()
	# 		response.user.todolist.add(t)

		
	# 	context = {"form":form}
	# 	return render(request, "main/create.html", context)