---
layout: page
title: Tutorials
header-img: "img/archive-bg.jpg"
---
<div class="page-content wc-container">
  	{% for post in site.posts %}
  		{% if post.categories contains 'tutorial' %}
		    {% capture currentyear %}{{post.date | date: "%Y"}}{% endcapture %}
		    {% if currentyear != year %}
		      {% unless forloop.first %}</ul>{% endunless %}
		        <h4>{{ currentyear }}</h4>
		        <ul class="posts">
		        {% capture year %}{{currentyear}}{% endcapture %} 
		    {% endif %}
		    <li><a href="{{ post.url | prepend: site.baseurl }}"><b>{{ post.title }} </b> | <i>{{ post.date | date: "%b %-d, %Y" }} </i>  </a></li>
		{% endif %}
	{% endfor %}
</ul>
</div>

<br>

<i>Header Image - "<b>Oldfashioned archiving of drawings</b>" by <b>Pieter van Marion</b> via <a href="https://flic.kr/p/p3rDGd"><u>Flickr</u></a><i> <br>


