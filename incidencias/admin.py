from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.core.exceptions import ValidationError

from .models import Especialidad, Incidencia


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label='Grupos'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'groups')

    def clean_groups(self):
        groups = self.cleaned_data.get('groups')
        if not groups:
            raise ValidationError('Debes asignar al menos un grupo.')
        return groups


class EspecialidadInline(admin.StackedInline):
    model = Especialidad
    extra = 0
    can_delete = False
    fields = ('usuario', 'especialidad')
    readonly_fields = ('usuario',)
    verbose_name = 'Especialidades'
    verbose_name_plural = 'Especialidades'

    def usuario(self, obj):
        return obj.usuario.username

    usuario.short_description = 'Usuario'


admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'groups'),
        }),
    )

    def get_inlines(self, request, obj):
        """
        El inline SOLO aparece si el usuario YA ES técnico en BD.
        Nunca depende del formulario actual.
        """
        if not obj:
            return []

        if obj.groups.filter(name='Técnicos').exists():
            return [EspecialidadInline]

        return []

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        try:
            grupo_tecnicos = Group.objects.get(name='Técnicos')
        except Group.DoesNotExist:
            return

        if grupo_tecnicos not in obj.groups.all():
            Especialidad.objects.filter(usuario=obj).delete()

    class Media:
        css = {
            'all': ('css/admin_fix.css',)
        }

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidad')

    def has_add_permission(self, request):
        return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'usuario':
            try:
                grupo_tecnicos = Group.objects.get(name='Técnicos')
                kwargs['queryset'] = grupo_tecnicos.user_set.all()
            except Group.DoesNotExist:
                pass
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'estado',
        'criticidad',
        'tipo_incidencia',
        'usuario_creador',
        'tecnico_asignado'
    )
    list_filter = ('estado', 'criticidad', 'tipo_incidencia')
    search_fields = ('titulo', 'descripcion')
