import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"arches76a"), "arches76a.urls", name="arches76a"),
)
