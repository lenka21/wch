var wchControllers = angular.module('wchControllers', []);


wchControllers.controller('CiostkoCtrl', ['$scope', '$http',
    function ($scope, $http) {
        $scope.helloWorldMsg = 'initialized';
        $http.get('ciostka.json').success(function(data){
            $scope.ciostka = data;
        });
    }
]);