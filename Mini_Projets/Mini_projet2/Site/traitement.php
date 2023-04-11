<?php
$bdd = new PDO('mysql:host=localhost;dbname=Archives;charset=utf8','root','chuck'); //connexion à la base de données
$nom = $_POST['nom']; //récupération de la saise dans le formulaire
$prenom = $_POST['prenom'];
$age = $_POST['age'];
$pays = $_POST['pays'];
$commune = $_POST['commune'];
$departement = $_POST['departement'];
$mois = $_POST['mois'];
$metier = $_POST['metier'];
$ecrire = $bdd->prepare("INSERT INTO Données VALUES ('$nom', '$prenom', '$age', '$pays', '$commune', '$departement', '$mois', '$metier');");
$ecrire->execute(); //exécution de la requête permettant d'écrire dans la basse de données
$months = array('janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'decembre');
foreach ($months as $mois) {
    $count = $bdd->prepare("SELECT COUNT(metier) FROM Données WHERE mois  = '$mois';"); //sélection du nombre de fois que "$mois" apparait
    $count->execute();
}
$data = $count->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <title>Formulaire HGGSP</title>
    <link rel="stylesheet" href="css/style2.css">
    <link rel="icon" href="miniDank4.png">
</head>
<body>
    <nav> <!-- même barre de navigation que l apage index.html avec les mêmes boutons-->
        <div class="navigation">
            <a href="index.html" style="text-decoration-line: none;">
                <div class="main">
                    <img src="Dank.png" class="nimg">
                    <div>Archives de 1914</div>
                </div>
            </a>
            <div class="else">
                <div class="elsetext">
                    <a href="index.html#how" class="comment">Comment ça marche ?</a>
                    <a href="#grah" class="comment">Graphiques</a>
                </div>
                <button class="formulaire">
                    <a href="index.html#form" style="text-decoration: none; color: #e5e5e5;">Formulaire</a>
                </button>
            </div>
        </div>
    </nav>
    <div style="margin-top: 80px; text-align: center; font-size: 1rem; line-height: 1; padding: 0.75rem;">
        <h1>Graphique représentant le nombre de personnes incorporées en fonction du mois :</h1>
    </div>
<div id="graph">
<canvas id="myChart" width="200" height="100"></canvas>
<script> /*javascript permettant la crétion du graphique */
const labels = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'] /*axe des abscisse*/
  const data = {
    labels: labels,
    datasets: [{
      label: 'Nombre de personne',
      data: <?php echo json_encode($data) ?>,
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(255, 159, 64, 0.2)',
        'rgba(255, 205, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(201, 203, 207, 0.2)'
      ],
      borderColor: [
        'rgb(255, 99, 132)',
        'rgb(255, 159, 64)',
        'rgb(255, 205, 86)',
        'rgb(75, 192, 192)',
        'rgb(54, 162, 235)',
        'rgb(153, 102, 255)',
        'rgb(201, 203, 207)'
      ],
      borderWidth: 1
    }]
  };

  const config = {
    type: 'bar',
    data: data,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    },
  };

  var myChart = new Chart( /*création du graphique*/
    document.getElementById('myChart'),
    config
  );
</script>
</div>
</body>
</html>