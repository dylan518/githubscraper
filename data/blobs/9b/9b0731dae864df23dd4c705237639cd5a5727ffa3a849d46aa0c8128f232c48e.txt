import it.unimi.dsi.fastutil.floats.Float2FloatFunction;
import java.util.List;
import java.util.Optional;
import java.util.function.BiPredicate;
import java.util.function.Supplier;
import javax.annotation.Nullable;

public class ckr extends cin<ctn> implements cql {
   public static final cwi b = cnf.aD;
   public static final cwm<cwg> c = cwe.bd;
   public static final cwf d = cwe.C;
   public static final int e = 1;
   protected static final int f = 1;
   protected static final int g = 14;
   protected static final dxj h = cjt.a(1.0, 0.0, 0.0, 15.0, 14.0, 15.0);
   protected static final dxj i = cjt.a(1.0, 0.0, 1.0, 15.0, 14.0, 16.0);
   protected static final dxj j = cjt.a(0.0, 0.0, 1.0, 15.0, 14.0, 15.0);
   protected static final dxj k = cjt.a(1.0, 0.0, 1.0, 16.0, 14.0, 15.0);
   protected static final dxj l = cjt.a(1.0, 0.0, 1.0, 15.0, 14.0, 15.0);
   private static final clq.b<ctn, Optional<bac>> m = new clq.b<ctn, Optional<bac>>() {
      public Optional<bac> a(ctn $$0, ctn $$1) {
         return Optional.of(new bab($$0, $$1));
      }

      public Optional<bac> a(ctn $$0) {
         return Optional.of($$0);
      }

      public Optional<bac> a() {
         return Optional.empty();
      }
   };
   private static final clq.b<ctn, Optional<bam>> n = new clq.b<ctn, Optional<bam>>() {
      public Optional<bam> a(final ctn $$0, final ctn $$1) {
         final bac $$2 = new bab($$0, $$1);
         return Optional.of(new bam() {
            @Nullable
            @Override
            public bwm createMenu(int $$0x, bub $$1x, buc $$2x) {
               if ($$0.d($$2) && $$1.d($$2)) {
                  $$0.e($$1.l);
                  $$1.e($$1.l);
                  return bwt.b($$0, $$1, $$2);
               } else {
                  return null;
               }
            }

            @Override
            public rq C_() {
               if ($$0.Y()) {
                  return $$0.C_();
               } else {
                  return (rq)($$1.Y() ? $$1.C_() : rq.c("container.chestDouble"));
               }
            }
         });
      }

      public Optional<bam> a(ctn $$0) {
         return Optional.of($$0);
      }

      public Optional<bam> a() {
         return Optional.empty();
      }
   };

   protected ckr(cvn.c $$0, Supplier<ctk<? extends ctn>> $$1) {
      super($$0, $$1);
      this.k(this.D.b().a(b, gy.c).a(c, cwg.a).a(d, Boolean.valueOf(false)));
   }

   public static clq.a g(cvo $$0) {
      cwg $$1 = $$0.c(c);
      if ($$1 == cwg.a) {
         return clq.a.a;
      } else {
         return $$1 == cwg.c ? clq.a.b : clq.a.c;
      }
   }

   @Override
   public cpp b_(cvo $$0) {
      return cpp.b;
   }

   @Override
   public cvo a(cvo $$0, gy $$1, cvo $$2, cgy $$3, gt $$4, gt $$5) {
      if ($$0.c(d)) {
         $$3.a($$4, dpw.c, dpw.c.a($$3));
      }

      if ($$2.a(this) && $$1.o().d()) {
         cwg $$6 = $$2.c(c);
         if ($$0.c(c) == cwg.a && $$6 != cwg.a && $$0.c(b) == $$2.c(b) && h($$2) == $$1.g()) {
            return $$0.a(c, $$6.a());
         }
      } else if (h($$0) == $$1) {
         return $$0.a(c, cwg.a);
      }

      return super.a($$0, $$1, $$2, $$3, $$4, $$5);
   }

   @Override
   public dxj a(cvo $$0, cgd $$1, gt $$2, dwv $$3) {
      if ($$0.c(c) == cwg.a) {
         return l;
      } else {
         switch(h($$0)) {
            case c:
            default:
               return h;
            case d:
               return i;
            case e:
               return j;
            case f:
               return k;
         }
      }
   }

   public static gy h(cvo $$0) {
      gy $$1 = $$0.c(b);
      return $$0.c(c) == cwg.b ? $$1.h() : $$1.i();
   }

   @Override
   public cvo a(ccx $$0) {
      cwg $$1 = cwg.a;
      gy $$2 = $$0.g().g();
      dpv $$3 = $$0.q().b_($$0.a());
      boolean $$4 = $$0.h();
      gy $$5 = $$0.k();
      if ($$5.o().d() && $$4) {
         gy $$6 = this.a($$0, $$5.g());
         if ($$6 != null && $$6.o() != $$5.o()) {
            $$2 = $$6;
            $$1 = $$6.i() == $$5.g() ? cwg.c : cwg.b;
         }
      }

      if ($$1 == cwg.a && !$$4) {
         if ($$2 == this.a($$0, $$2.h())) {
            $$1 = cwg.b;
         } else if ($$2 == this.a($$0, $$2.i())) {
            $$1 = cwg.c;
         }
      }

      return this.m().a(b, $$2).a(c, $$1).a(d, Boolean.valueOf($$3.a() == dpw.c));
   }

   @Override
   public dpv c_(cvo $$0) {
      return $$0.c(d) ? dpw.c.a(false) : super.c_($$0);
   }

   @Nullable
   private gy a(ccx $$0, gy $$1) {
      cvo $$2 = $$0.q().a_($$0.a().a($$1));
      return $$2.a(this) && $$2.c(c) == cwg.a ? $$2.c(b) : null;
   }

   @Override
   public void a(cgx $$0, gt $$1, cvo $$2, bcc $$3, cax $$4) {
      if ($$4.z()) {
         cti $$5 = $$0.c_($$1);
         if ($$5 instanceof ctn) {
            ((ctn)$$5).a($$4.x());
         }
      }

   }

   @Override
   public void a(cvo $$0, cgx $$1, gt $$2, cvo $$3, boolean $$4) {
      if (!$$0.a($$3.b())) {
         cti $$5 = $$1.c_($$2);
         if ($$5 instanceof bac) {
            baf.a($$1, $$2, (bac)$$5);
            $$1.c($$2, this);
         }

         super.a($$0, $$1, $$2, $$3, $$4);
      }
   }

   @Override
   public baj a(cvo $$0, cgx $$1, gt $$2, buc $$3, bai $$4, dwm $$5) {
      if ($$1.y) {
         return baj.a;
      } else {
         bam $$6 = this.b($$0, $$1, $$2);
         if ($$6 != null) {
            $$3.a($$6);
            $$3.b(this.c());
            bst.a($$3, true);
         }

         return baj.b;
      }
   }

   protected akd<abb> c() {
      return akg.i.b(akg.ao);
   }

   public ctk<? extends ctn> d() {
      return (ctk<? extends ctn>)this.a.get();
   }

   @Nullable
   public static bac a(ckr $$0, cvo $$1, cgx $$2, gt $$3, boolean $$4) {
      return (bac)((Optional)$$0.a($$1, $$2, $$3, $$4).apply(m)).orElse(null);
   }

   @Override
   public clq.c<? extends ctn> a(cvo $$0, cgx $$1, gt $$2, boolean $$3) {
      BiPredicate<cgy, gt> $$4;
      if ($$3) {
         $$4 = ($$0x, $$1x) -> false;
      } else {
         $$4 = ckr::a;
      }

      return clq.a((ctk<? extends ctn>)this.a.get(), ckr::g, ckr::h, b, $$0, $$1, $$2, $$4);
   }

   @Nullable
   @Override
   public bam b(cvo $$0, cgx $$1, gt $$2) {
      return (bam)((Optional)this.a($$0, $$1, $$2, false).apply(n)).orElse(null);
   }

   public static clq.b<ctn, Float2FloatFunction> a(final cue $$0) {
      return new clq.b<ctn, Float2FloatFunction>() {
         public Float2FloatFunction a(ctn $$0x, ctn $$1) {
            return $$2 -> Math.max($$0.a($$2), $$1.a($$2));
         }

         public Float2FloatFunction a(ctn $$0x) {
            return $$0::a;
         }

         public Float2FloatFunction a() {
            return $$0::a;
         }
      };
   }

   @Override
   public cti a(gt $$0, cvo $$1) {
      return new ctn($$0, $$1);
   }

   @Nullable
   @Override
   public <T extends cti> ctj<T> a(cgx $$0, cvo $$1, ctk<T> $$2) {
      return $$0.y ? a($$2, this.d(), ctn::a) : null;
   }

   public static boolean a(cgy $$0, gt $$1) {
      return a((cgd)$$0, $$1) || b($$0, $$1);
   }

   private static boolean a(cgd $$0, gt $$1) {
      gt $$2 = $$1.b();
      return $$0.a_($$2).g($$0, $$2);
   }

   private static boolean b(cgy $$0, gt $$1) {
      List<bnh> $$2 = $$0.a(
         bnh.class, new dwl((double)$$1.u(), (double)($$1.v() + 1), (double)$$1.w(), (double)($$1.u() + 1), (double)($$1.v() + 2), (double)($$1.w() + 1))
      );
      if (!$$2.isEmpty()) {
         for(bnh $$3 : $$2) {
            if ($$3.fJ()) {
               return true;
            }
         }
      }

      return false;
   }

   @Override
   public boolean d_(cvo $$0) {
      return true;
   }

   @Override
   public int a(cvo $$0, cgx $$1, gt $$2) {
      return bwm.b(a(this, $$0, $$1, $$2, false));
   }

   @Override
   public cvo a(cvo $$0, cpw $$1) {
      return $$0.a(b, $$1.a($$0.c(b)));
   }

   @Override
   public cvo a(cvo $$0, coh $$1) {
      return $$0.a($$1.a($$0.c(b)));
   }

   @Override
   protected void a(cvp.a<cjt, cvo> $$0) {
      $$0.a(b, c, d);
   }

   @Override
   public boolean a(cvo $$0, cgd $$1, gt $$2, dqm $$3) {
      return false;
   }

   @Override
   public void a(cvo $$0, agg $$1, gt $$2, amn $$3) {
      cti $$4 = $$1.c_($$2);
      if ($$4 instanceof ctn) {
         ((ctn)$$4).i();
      }

   }
}
