from django.http import Http404
from rest_framework.views import APIView
from course.models import Branch
from course.api.serializers import BranchSerializer
from rest_framework.response import Response
from rest_framework import status


class BranchAPIView(APIView):

    def get(self, request, format=None):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            branch = Branch.objects.get(pk=pk)
            return branch
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchSerializer(instance=branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        branch = self.get_object(pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
