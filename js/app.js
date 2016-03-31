var wchApp = angular.module('wchApp', [
  'ngRoute',
  'wchControllers',
  'bootstrapSubmenu'
]);

wchApp.config(['$routeProvider',
  function($routeProvider) {


    $routeProvider
      .when('/home', {
        templateUrl: 'templates/home/home.html',
        controller: 'HomeCtrl'
      })
      .when('/sales', {
        templateUrl: 'templates/sales/sales.html',
        controller: 'HomeCtrl'
      })
      .when('/terms', {
        templateUrl: 'templates/terms/terms.html',
        controller: 'HomeCtrl'
      })
      .when('/reviewers', {
        templateUrl: 'templates/reviewers/reviewers.html',
        controller: 'HomeCtrl'
      })
      .when('/abstract', {
        templateUrl: 'templates/abstract/abstract.html',
        controller: 'AbstractCtrl'
      })
      .when('/home', {
        templateUrl: 'templates/home/home.html',
        controller: 'HomeCtrl'
      })
      .when('/editor', {
        templateUrl: 'templates/editor/editor.html',
        controller: 'HomeCtrl'
      })
      .when('/#abstarct', {
        templateUrl: 'templates/abstract/abstract.html',
        controller: 'AbstractCtrl'
      })
      .when('/procedures', {
        templateUrl: 'templates/procedures/procedures.html',
        controller: 'HomeCtrl'
      })
      .when('/contact', {
        templateUrl: 'templates/contact/contact.html',
        controller: 'HomeCtrl'
      })
      .otherwise({
        redirectTo: '/home'
      });
  }]);