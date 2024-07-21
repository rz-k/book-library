from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from booklibrary.api.mixins import ApiAuthMixin
from drf_spectacular.utils import extend_schema

from booklibrary.book.serializers.book_serializers import (
    OutPutBookSerializer, BookFilterSerializer
)

from booklibrary.book.services.suggest_services import (
    SuggestService,
)
from booklibrary.utils.pagination import LimitOffsetPagination


@extend_schema(tags=['books'])
class SuggestApi(ApiAuthMixin, APIView, LimitOffsetPagination):
    @extend_schema(responses=OutPutBookSerializer, parameters=[BookFilterSerializer])
    def get(self, request):
        filters_serializer = BookFilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        
        query = SuggestService.suggest_book_list(user=request.user, filters=filters_serializer.validated_data)

        if not query:
            return Response("there is not enogh data about you", status=status.HTTP_200_OK)

        pagination = self.paginate_queryset(query, self.request)               
        serializer = OutPutBookSerializer(pagination, many=True, context={"request":request})
        response = self.get_paginated_data(serializer.data)
        return Response(response, status=status.HTTP_200_OK)
