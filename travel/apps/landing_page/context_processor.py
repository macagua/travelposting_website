def get_ip(request):
   return {'ip' : request.META['REMOTE_ADDR']}
