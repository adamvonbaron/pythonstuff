<%include file="root.mako" />

<div class="container">
    <div class="row d-flex align-items-center justify-content-center">
        <p>${user}'s starred repos</p>
    </div>
    <div class="row">
    <ul class="list-group">
        % for repo in repos:
            <li class="list-group-item">
                <a href=${repo['url']}>${repo['name']}</a>
            </li>
        % endfor
    </ul>
  </div>
</div>