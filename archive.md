---
layout: page
title: Archive
header-img: "img/archive-bg.jpg"
---
<div class="page-content wc-container">
  <h1>Blog Archive</h1>  
  {% for post in site.posts %}
    {% capture currentyear %}{{post.date | date: "%Y"}}{% endcapture %}
    {% if currentyear != year %}
      {% unless forloop.first %}</ul>{% endunless %}
        <h4>{{ currentyear }}</h4>
        <ul class="posts">
        {% capture year %}{{currentyear}}{% endcapture %} 
      {% endif %}
    <li><a href="{{ post.url | prepend: site.baseurl }}"><b>{{ post.title }} </b> | {{ post.date | date: "%b %-d, %Y" }}  </a></li>
{% endfor %}
</div>

<br><br>

<i>Image - <b>"Oldfashioned archiving of drawings"</b> by <b>Pieter van Marion</b> via <a href="https://flic.kr/p/p3rDGd">Flickr</a><i> <br>