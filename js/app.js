var wchApp = angular.module('wchApp', [
  'ngRoute',
  'wchControllers'
]);

wchApp.config(['$routeProvider',
  function($routeProvider) {




    $routeProvider.
      when('/ciostko', {
        templateUrl: 'ciostko.html',
        controller: 'CiostkoCtrl'
      }).
      otherwise({
        redirectTo: '/ciostko'
      });
  }]);