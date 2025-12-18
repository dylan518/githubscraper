package com.example.TestTask.Entities.Structures;

import com.example.TestTask.Entities.TransportKind;

import java.util.List;

public class KindNode {
    List<TypeNode> typeNodes;
    TransportKind kind;

    public TransportKind getKind() {
        return kind;
    }

    public void setKind(TransportKind kind) {
        this.kind = kind;
    }

    public KindNode(List<TypeNode> typeNodes, TransportKind kind) {
        this.typeNodes = typeNodes;
        this.kind = kind;
    }

    public void setTypeNodes(List<TypeNode> typeNodes) {
        this.typeNodes = typeNodes;
    }

    public List<TypeNode> getTypeNodes() {
        return typeNodes;
    }
}
