This is ${foo}
Copyright Linus Torvalds ${years(2007)}

% for a in range(10):
	${a}
% endfor

<%
	import platform # for node
	hostname=platform.node()
%>

You are running on ${hostname}

This checks if a variable is in a mako dict or not...
http://stackoverflow.com/questions/18624290/how-to-check-if-a-key-exists-in-mako-dict
% if 'a' in d:
	${d['a']}
	'a' is in d
% else:
	'a' is not in d
% endif
