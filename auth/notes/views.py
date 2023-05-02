from rest_framework.views import APIView
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Note



# Create your views here.
class NoteCollectionView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self,request):
        """List"""
        notes = request.user.notes.all()
        serializer = self.serializer_class(instance=notes, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)




 
    def post(self,request):
        """Create"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)



class NoteSingletoneView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self, request, pk):
        """Detail"""
        note = get_object_or_404(Note, pk=pk)
        serializer = self.serializer_class(instance=note)

        return Response(serializer.data)





    def patch(self,request,pk):
        """Update"""
        note = get_object_or_404(Note, pk=pk)

        serializer = self.serializer_class(data=request.data, instance=note, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)






    def delete(self, request, pk):
        """Delete"""
        note = get_object_or_404(Note, pk=pk)

        note.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
