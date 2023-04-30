{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>youha</title>
  <!-- fontawesome css cdn-->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
      integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w=="
      crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- fontawesome css cdn-->
  <link rel="stylesheet" href="{% static 'css/fontawesome.css' %}">
  <!-- normalize css cdn-->
  <link rel="stylesheet" href="{% static 'css/normalize.css' %}">
  <!-- global css -->
  <link rel="stylesheet" href="{%static 'css/style.css'%}">
  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
</head>

<body class="list-page">
    <header>
        {% include 'partials/navbar.html' %}
    </header>
    <div class="title-area">
        <h2 class="page-title">Youtuber List</h2>
    </div>
    <div class="search-area">
      <form  method="GET">
        {% csrf_token %}
        <div class="search-bar">
            <input type="text" name="search" id="search-bar" placeholder="유튜버를 검색해주세요!">
            <button type="submit" class="search-btn">검색</button>
        </div>
    </form>
    </div>

    <div class="content">
        <main class="list-area skill" >
            <div id="youtuber" >
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
                          구독자 수 :&nbsp;
                          <span v-text="item.subscribers.toLocaleString('en-US')"></span>
                          {{item.subscribers}}명
                        </h3>
                      </ul>
                  </div>
                  </li>
                </ul>
              </div>

              <template>
                <div>
                  <ul>
                    <li v-for="(item, index) in items" :key="index">{{ item }}</li>
                  </ul>
                  <div>
                    <button v-for="n in totalPages" :key="n" @click="getPage(n)">{{ n }}</button>
                  </div>
                </div>
              </template>


        </main>
    </div>


    {% include 'partials/footer.html' %}



<script>
new Vue({
  el: '#youtuber',
  data: {
    items: []
  },
  mounted() {
    axios.get('/api/v1/youtuber/?page=1')
      .then(response => {
        this.items = response.data['results'];
        console.log(this.items);
      })
  }
})
</script>
  
</body>

<style>
  ul {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    list-style-type: none; 
  }
  
  li {
    width: calc(33.33% - 10px);
    margin-bottom: 20px; 
  }
</style>

</html>