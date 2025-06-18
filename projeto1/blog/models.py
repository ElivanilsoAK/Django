from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    pub_date = models.DateTimeField('data de publicação')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    com_date = models.DateTimeField('data do comentário')

    def __str__(self):
        return f'Comentário de {self.post.titulo}: {self.texto[:50]}...' # Exibe os primeiros 50 caracteres