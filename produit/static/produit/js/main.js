var ProduitsListPage = {
	init: function() {
		this.$container = $('.Produits-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-heart', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};
var ProduitsListPage1 = {
	init: function() {
		this.$container = $('.Produits-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.fa-smile-o', self).toggleClass('active');
				}

			});

			return false;
		});
	}
};
$(document).ready(function() {
	ProduitsListPage1.init();
	ProduitsListPage.init();
});