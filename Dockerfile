FROM nginx:alpine

# Copie la page HTML dans le dossier servi par nginx
COPY index.html /usr/share/nginx/html/index.html

# Expose le port 8080
EXPOSE 8080

# Redirige nginx sur le port 8080 (pas besoin de root)
RUN sed -i 's/listen\s*80;/listen 8080;/g' /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
