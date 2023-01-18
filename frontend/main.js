const vue = {
  create : function(props) {
    var app = new Vue(props);
    app.mount("#app");
    return app;
  }
};