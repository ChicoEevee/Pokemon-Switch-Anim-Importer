# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Anim

import flatbuffers
from flatbuffers.compat import import_numpy

from GFLib.Anim.ByteDataTrack import ByteDataTrackT
from GFLib.Anim.DataTrack import DataTrackCreator
from GFLib.Anim.FloatDataTrack import FloatDataTrackT
from GFLib.Anim.IntDataTrack import IntDataTrackT
from GFLib.Anim.StringDataTrack import StringDataTrackT

np = import_numpy()

class CommandEntry(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CommandEntry()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCommandEntry(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CommandEntry
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CommandEntry
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CommandEntry
    def TracksType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # CommandEntry
    def Tracks(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def CommandEntryStart(builder):
    builder.StartObject(3)

def Start(builder):
    CommandEntryStart(builder)

def CommandEntryAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    CommandEntryAddName(builder, name)

def CommandEntryAddTracksType(builder, tracksType):
    builder.PrependUint8Slot(1, tracksType, 0)

def AddTracksType(builder, tracksType):
    CommandEntryAddTracksType(builder, tracksType)

def CommandEntryAddTracks(builder, tracks):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(tracks), 0)

def AddTracks(builder, tracks):
    CommandEntryAddTracks(builder, tracks)

def CommandEntryEnd(builder):
    return builder.EndObject()

def End(builder):
    return CommandEntryEnd(builder)

try:
    from typing import Union
except:
    pass

class CommandEntryT(object):

    # CommandEntryT
    def __init__(self):
        self.name = None  # type: str
        self.tracksType = 0  # type: int
        self.tracks = None  # type: Union[None, IntDataTrackT, FloatDataTrackT, ByteDataTrackT, StringDataTrackT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        commandEntry = CommandEntry()
        commandEntry.Init(buf, pos)
        return cls.InitFromObj(commandEntry)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, commandEntry):
        x = CommandEntryT()
        x._UnPack(commandEntry)
        return x

    # CommandEntryT
    def _UnPack(self, commandEntry):
        if commandEntry is None:
            return
        self.name = commandEntry.Name()
        self.tracksType = commandEntry.TracksType()
        self.tracks = DataTrackCreator(self.tracksType, commandEntry.Tracks())

    # CommandEntryT
    def Pack(self, builder):
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.tracks is not None:
            tracks = self.tracks.Pack(builder)
        CommandEntryStart(builder)
        if self.name is not None:
            CommandEntryAddName(builder, name)
        CommandEntryAddTracksType(builder, self.tracksType)
        if self.tracks is not None:
            CommandEntryAddTracks(builder, tracks)
        commandEntry = CommandEntryEnd(builder)
        return commandEntry