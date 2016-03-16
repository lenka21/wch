var wchControllers = angular.module('wchControllers', []);


wchControllers.controller('CiostkoCtrl', ['$scope', '$http',
    function ($scope, $http) {
        $scope.helloWorldMsg = 'initialized';
        $http.get('ciostka.json').success(function(data){
            $scope.ciostka = data;
        });
    }
]);

wchControllers.controller('HomeCtrl', ['$scope', '$http',
    function ($scope, $http) {
    }
]);

wchControllers.controller('AbstractCtrl', ['$scope', '$http',
    function ($scope, $http) {
        $http.get('abstracts.json').success(function(data){
            $scope.abstracts = data;
        });
    }
]);