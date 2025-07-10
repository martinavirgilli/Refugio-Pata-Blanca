from rest_framework.permissions import BasePermission

class TienePermisoModelo(BasePermission):
    """
    Verifica si el usuario tiene permiso para realizar una acción sobre el modelo asociado a la vista.
    """

    def has_permission(self, request, view):
        # modelo definido vistas
        if not hasattr(view, 'model'):
            return False

        model = view.model
        app_label = model._meta.app_label
        model_name = model._meta.model_name

        metodo_permiso = {
            'GET': f'{app_label}.view_{model_name}',
            'POST': f'{app_label}.add_{model_name}',
            'PUT': f'{app_label}.change_{model_name}',
            'PATCH': f'{app_label}.change_{model_name}',
            'DELETE': f'{app_label}.delete_{model_name}',
        }

        permiso = metodo_permiso.get(request.method)
        if permiso:
            return request.user.has_perm(permiso)
        return False