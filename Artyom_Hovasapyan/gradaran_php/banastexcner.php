<?php include 'php_lracumner/head.php'; ?>
<head>
	<link rel="stylesheet" href="css/banastexcner.css">
</head>
<body>

<header id="home_" >
	<?php include 'php_lracumner/header.php'; ?>
</header>

<section class="second_section">
   <div class="container">
      <div class="d-flex row centered" >
         <?php
				include "php_lracumner/banastexcner_add.php";
				include "php_lracumner/banastexcutyunneri_tip.php";
			?>
			<form  method="post">

				<input id='url_stugum' type="hidden" name="url_stugum" value="">
				<!-- <input id='tr' type="hidden" name="url_anun" value="">
				<input id='tr' type="hidden" name="url_azganun" value=""> -->


			</form>

      </div>

   </div>
</section>
<script src="js/banastexcner.js"></script>
</body>
