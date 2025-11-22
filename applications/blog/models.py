from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField("Nombre", max_length=50, unique=True)
    slug = models.SlugField("Slug", unique=True)

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", unique=True)

    # Imagen principal
    main_image = models.ImageField(
        "Imagen principal",
        upload_to="blog/",
        blank=True,
        null=True
    )

    # Etiquetas (Django, Python, CSS, IA, etc)
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Etiquetas",
        blank=True,
        related_name="posts",
    )

    excerpt = models.TextField("Resumen", max_length=400, blank=True)
    content = models.TextField("Contenido")

    published_at = models.DateTimeField("Fecha de publicación", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado", auto_now=True)
    is_published = models.BooleanField("Publicado", default=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title