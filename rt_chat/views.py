from django.shortcuts import render


def chat_room(request, label):
# if room with given label DNE, automatically create it
# upon first visit (a la etehrpad)
	room, created = Room.objects.get_or_create(label=label)

	# want to show last 50 msgs, ordered most-recent-last
	messages = reversed(room.messages.order_by('-timestamp')[:50])

	return render(request, "chat/room.html", {
		'room':room,
		'messages':messages,
	})