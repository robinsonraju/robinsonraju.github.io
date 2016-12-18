---
layout: page
title: Papers
header-img: "img/research-bg.jpg"
---
<div class="page-content wc-container">
  	{% for post in site.posts %}
  		{% if post.categories contains 'paper' %}
		    {% capture currentyear %}{{post.date | date: "%Y"}}{% endcapture %}
		    {% if currentyear != year %}
		      {% unless forloop.first %}{% endunless %}
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

<i>Header Image - "<b>Research</b>" by <b>Thomas Haynie / Phlebotomy Tech</b> via <a href="https://flic.kr/p/tX2tGj"><u>Flickr</u></a><i> <br>


