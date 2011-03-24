/**
 * Gulu Facebook module js
 *
 */

var Facebook = Facebook || {};

Facebook = function() {
    
};

Facebook.prototype = {
    // checks if the user is logged in, if not logs them in
    doLoginCheck: function() {
        FB.getLoginStatus(function(response) {
            if(response.session) {
                this.doLoginRedirect();
            }
            else{
                this.login();
            }
        });
    },          
    
    // logs the user in and redirects to the url in ?next=
    doLogin: function(redirect) {
        FB.login(
        $.proxy(function(response) {
            if(response.session) {
                this.doLoginRedirect(redirect);
            }
            else {
                return;
            }
        }, this),
        {
            perms: 'offline_access,email',
        });
    },
    
    doLoginRedirect: function(redirect_url) {
        if(redirect_url == undefined){
            redirect_url = Gulu.getUrlParameter('next');
        }   
        if(redirect_url != "") {
            Gulu.redirect(redirect_url);
        }
        else {
            Gulu.redirect("/signup");
        }
    },
  
};

    