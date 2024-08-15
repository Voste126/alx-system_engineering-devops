# A puppet manuscript to replace a line in a file on a server

exec { 'fix-wordpress':
  command => '/usr/bin/touch /var/www/html/wp-content/themes/twentyseventeen/assets/images/header.jpg',
}