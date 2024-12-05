# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Anim

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Framed8ByteTrack(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Framed8ByteTrack()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFramed8ByteTrack(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Framed8ByteTrack
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Framed8ByteTrack
    def Frames(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Framed8ByteTrack
    def FramesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Framed8ByteTrack
    def FramesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Framed8ByteTrack
    def FramesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Framed8ByteTrack
    def Byte(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Framed8ByteTrack
    def ByteAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Framed8ByteTrack
    def ByteLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Framed8ByteTrack
    def ByteIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Framed8ByteTrackStart(builder):
    builder.StartObject(2)

def Start(builder):
    Framed8ByteTrackStart(builder)

def Framed8ByteTrackAddFrames(builder, frames):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(frames), 0)

def AddFrames(builder, frames):
    Framed8ByteTrackAddFrames(builder, frames)

def Framed8ByteTrackStartFramesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartFramesVector(builder, numElems):
    return Framed8ByteTrackStartFramesVector(builder, numElems)

def Framed8ByteTrackAddByte(builder, byte):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(byte), 0)

def AddByte(builder, byte):
    Framed8ByteTrackAddByte(builder, byte)

def Framed8ByteTrackStartByteVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartByteVector(builder, numElems):
    return Framed8ByteTrackStartByteVector(builder, numElems)

def Framed8ByteTrackEnd(builder):
    return builder.EndObject()

def End(builder):
    return Framed8ByteTrackEnd(builder)

try:
    from typing import List
except:
    pass

class Framed8ByteTrackT(object):

    # Framed8ByteTrackT
    def __init__(self):
        self.frames = None  # type: List[int]
        self.byte = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        framed8ByteTrack = Framed8ByteTrack()
        framed8ByteTrack.Init(buf, pos)
        return cls.InitFromObj(framed8ByteTrack)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, framed8ByteTrack):
        x = Framed8ByteTrackT()
        x._UnPack(framed8ByteTrack)
        return x

    # Framed8ByteTrackT
    def _UnPack(self, framed8ByteTrack):
        if framed8ByteTrack is None:
            return
        if not framed8ByteTrack.FramesIsNone():
            if np is None:
                self.frames = []
                for i in range(framed8ByteTrack.FramesLength()):
                    self.frames.append(framed8ByteTrack.Frames(i))
            else:
                self.frames = framed8ByteTrack.FramesAsNumpy()
        if not framed8ByteTrack.ByteIsNone():
            if np is None:
                self.byte = []
                for i in range(framed8ByteTrack.ByteLength()):
                    self.byte.append(framed8ByteTrack.Byte(i))
            else:
                self.byte = framed8ByteTrack.ByteAsNumpy()

    # Framed8ByteTrackT
    def Pack(self, builder):
        if self.frames is not None:
            if np is not None and type(self.frames) is np.ndarray:
                frames = builder.CreateNumpyVector(self.frames)
            else:
                Framed8ByteTrackStartFramesVector(builder, len(self.frames))
                for i in reversed(range(len(self.frames))):
                    builder.PrependUint8(self.frames[i])
                frames = builder.EndVector()
        if self.byte is not None:
            if np is not None and type(self.byte) is np.ndarray:
                byte = builder.CreateNumpyVector(self.byte)
            else:
                Framed8ByteTrackStartByteVector(builder, len(self.byte))
                for i in reversed(range(len(self.byte))):
                    builder.PrependUint8(self.byte[i])
                byte = builder.EndVector()
        Framed8ByteTrackStart(builder)
        if self.frames is not None:
            Framed8ByteTrackAddFrames(builder, frames)
        if self.byte is not None:
            Framed8ByteTrackAddByte(builder, byte)
        framed8ByteTrack = Framed8ByteTrackEnd(builder)
        return framed8ByteTrack