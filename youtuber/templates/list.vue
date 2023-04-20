{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ofcourse</title>
    <!-- fontawesome css cdn-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
        integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <!-- normalize css cdn-->
    <!-- <link rel="stylesheet" href="{% static 'css/normalize.css' %}"> -->
    <!-- global css -->
    <link rel="stylesheet" href="{%static 'css/style.css'%}">
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>

<body class="list-page">
    <header>
        {% include 'partials/navbar.html' %}
    </header>
    <div class="title-area">
        <h2 class="page-title">youha</h2>
    </div>

    <div class="content">
        <main class="list-area skill">
            <div id="youtuber">
                <ul class="list-container">
                  <li v-for="item in items" class="list-card">
                    <div class="company-icon">
                      <a :href="item.link">
                        <img :src="item.imgUrl" alt="이미지" style="border-radius: 50%;">
                      </a>
                    </div>
                    <div class="info-box">
                      <h3 v-text="item.name">{{item.name}}</h3>
                    </div>
                    <p class="skill-info">
                      youha
                    </p>
                    <div class="skill-list">
                      <ul>
                        <h3>
                          구독자 수 :
                          <span v-text="item.subscribers"></span>
                          {{ item.subscribers }}
                        </h3>
                      </ul>
                  </div>
                  </li>
                </ul>
              </div>
        </main>
    </div>

    <footer>
        <p>
            Copyright © 2023. WOOKIMODO All Rights Reserved.
        </p>
    </footer>
<script src="{%static 'js/index.js'%}"></script>
<script>
new Vue({
  el: '#youtuber',
  data: {
    items: []
  },
  mounted() {
    axios.get('/api/youtuber/?page=1')
      .then(response => {
        this.items = response.data['results'];
        console.log(this.items);
      })
  }
})
</script>
</body>

</html>